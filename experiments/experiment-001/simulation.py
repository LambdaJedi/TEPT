"""
TEPT Experiment 001 (v2: paired random numbers)
How does a change in departure time affect the interaction of two vehicles
approaching a shared intersection?

Spec v0.1 alignment:
  - Intervention a: shift Vehicle B's departure by `offset` seconds.
  - Outcome Y = 1 if the two vehicles' arrival times at the intersection are
    within CONFLICT_WINDOW seconds of each other (a simple proxy for
    overlapping conflict-zone occupancy).
  - Common random numbers: every scenario re-uses the SAME random speed and
    delay draws, so differences between scenarios are caused by the
    intervention and not by sampling noise.
  - Reports P_hat(Y | do(a)), delta P = P(a) - P(baseline) with a paired 95% CI,
    mean/min arrival gap, and the marginal effect per step (for H2).

Run:  python simulation.py
"""

import csv
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ---------------- Parameters ----------------
SEED = 42
N_RUNS = 20_000
DISTANCE_M = 1500.0
MEAN_SPEED_MS = 13.9       # ~50 km/h
SPEED_SD_MS = 1.8
DELAY_SD_S = 6.0           # half-normal delay (lights, traffic)
CONFLICT_WINDOW_S = 4.0
OFFSETS_S = list(range(0, 65, 5))   # offset 0 = baseline
HIGHLIGHT_OFFSET_S = 30

OUT_DIR = "results"


def draw_trip_components(rng, n):
    """Random travel time (s) for n trips, excluding departure time."""
    speed = np.clip(rng.normal(MEAN_SPEED_MS, SPEED_SD_MS, n), 4.0, None)
    delay = np.abs(rng.normal(0, DELAY_SD_S, n))
    return DISTANCE_M / speed + delay


def conflict(arrive_a, arrive_b):
    return np.abs(arrive_a - arrive_b) < CONFLICT_WINDOW_S


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    rng = np.random.default_rng(SEED)

    # Draw once, reuse for every scenario (common random numbers).
    travel_a = draw_trip_components(rng, N_RUNS)
    travel_b = draw_trip_components(rng, N_RUNS)
    arrive_a = travel_a  # A departs at t = 0

    base_hit = conflict(arrive_a, travel_b)  # baseline: offset 0
    rows, samples = [], {}
    prev_p = None
    for off in OFFSETS_S:
        arrive_b = travel_b + off
        hit = conflict(arrive_a, arrive_b)
        p = hit.mean()
        se = np.sqrt(p * (1 - p) / N_RUNS)
        d = hit.astype(float) - base_hit.astype(float)       # paired difference
        dp, dse = d.mean(), d.std(ddof=1) / np.sqrt(N_RUNS)
        gap = np.abs(arrive_b - arrive_a)
        rows.append({
            "offset_s": off,
            "interaction_prob": round(p, 4),
            "ci95_low": round(max(0.0, p - 1.96 * se), 4),
            "ci95_high": round(min(1.0, p + 1.96 * se), 4),
            "delta_p_vs_baseline": round(dp, 4),
            "delta_p_ci95_low": round(dp - 1.96 * dse, 4),
            "delta_p_ci95_high": round(dp + 1.96 * dse, 4),
            "mean_abs_gap_s": round(gap.mean(), 2),
            "min_abs_gap_s": round(gap.min(), 3),
            "marginal_dp_per_step": "" if prev_p is None else round(p - prev_p, 4),
        })
        prev_p = p
        samples[off] = (arrive_a, arrive_b)

    with open(os.path.join(OUT_DIR, "summary.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    # ---- Plot 1: arrival distributions ----
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), sharey=True)
    for ax, off, title in [
        (axes[0], 0, "Baseline (B departs with A)"),
        (axes[1], HIGHLIGHT_OFFSET_S, f"B departs {HIGHLIGHT_OFFSET_S}s later"),
    ]:
        a, b = samples[off]
        bins = np.linspace(80, 190, 70)
        ax.hist(a, bins=bins, alpha=0.6, label="Vehicle A", color="#2b6cb0")
        ax.hist(b, bins=bins, alpha=0.6, label="Vehicle B", color="#dd6b20")
        ax.set_title(f"{title}\ninteraction probability = {conflict(a, b).mean():.1%}")
        ax.set_xlabel("Arrival time at intersection (s)")
        ax.legend()
    axes[0].set_ylabel("Simulated trips")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "arrival_times.png"), dpi=150)
    plt.close(fig)

    # ---- Plot 2: interaction probability vs offset ----
    offs = [r["offset_s"] for r in rows]
    ps = np.array([r["interaction_prob"] for r in rows])
    lo = np.array([r["ci95_low"] for r in rows])
    hi = np.array([r["ci95_high"] for r in rows])
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(offs, ps, marker="o", color="#2b6cb0")
    ax.fill_between(offs, lo, hi, alpha=0.25, color="#2b6cb0")
    ax.axvline(HIGHLIGHT_OFFSET_S, ls="--", color="grey")
    ax.set_xlabel("Departure offset of Vehicle B (s)")
    ax.set_ylabel("Interaction probability")
    ax.set_title(f"Effect of departure timing on interaction "
                 f"(window = {CONFLICT_WINDOW_S:.0f}s, n = {N_RUNS:,}, paired draws)")
    ax.set_ylim(0, max(0.05, ps.max() * 1.15))
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "interaction_vs_offset.png"), dpi=150)
    plt.close(fig)

    # ---- Plot 3: marginal effect per 5 s step (H2: is the effect proportional?) ----
    steps = [r["marginal_dp_per_step"] for r in rows[1:]]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar([str(o) for o in offs[1:]], steps, color="#dd6b20")
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xlabel("Offset reached (s); each bar = change from the previous 5 s step")
    ax.set_ylabel("Change in interaction probability")
    ax.set_title("Unequal propagation (H2): effect of each extra 5 s of delay")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "marginal_effect.png"), dpi=150)
    plt.close(fig)

    print(f"{'offset':>7} {'P(Y)':>7} {'dP vs base':>11} {'95% CI of dP':>20} {'step dP':>8}")
    for r in rows:
        print(f"{r['offset_s']:>6}s {r['interaction_prob']:>7.1%} "
              f"{r['delta_p_vs_baseline']:>+11.1%} "
              f"[{r['delta_p_ci95_low']:+.1%}, {r['delta_p_ci95_high']:+.1%}] "
              f"{'' if r['marginal_dp_per_step']=='' else format(r['marginal_dp_per_step'], '+.1%'):>8}")


if __name__ == "__main__":
    main()
