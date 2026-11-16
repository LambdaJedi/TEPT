# TEPT Experiment 001: Departure timing and two-vehicle interaction

**Question:** How does shifting one vehicle's departure time (e.g. by 30 seconds) change the chance that two vehicles interact at a shared intersection?

Hypotheses addressed: **H1** (temporal sensitivity) and a first look at **H2** (unequal propagation). See `../../research/hypotheses.md`.

## Method

A Monte Carlo simulation (`simulation.py`; Python, NumPy, Matplotlib):

- Vehicles A and B each start 1,500 m from the intersection.
- Average speed per trip ~ Normal(13.9 m/s, about 50 km/h; sd 1.8 m/s).
- Random delay per trip (lights, traffic) ~ half-normal, sd 6 s.
- Arrival time = departure + distance / speed + delay.
- **Outcome Y = 1 (interaction)** when the two arrival times are less than 4 s apart.
- A departs at t = 0. B departs at offsets 0 to 60 s in 5 s steps. Offset 0 is the baseline.
- 20,000 trials per scenario, seed 42.
- **Paired random numbers:** all scenarios reuse the same random draws, so differences between them come from the intervention, not sampling noise. This follows the matched-seed decision in spec v0.1.

## Run it

```
pip install -r ../../requirements.txt
python simulation.py
```

Outputs in `results/`: `summary.csv`, `arrival_times.png`, `interaction_vs_offset.png`, `marginal_effect.png`.

## Results (seed 42)

| B departs later by | P(interaction) | Change vs baseline (95% CI, paired) |
| --- | --- | --- |
| 0 s (baseline) | 15.4% | n/a |
| 15 s | 11.4% | -4.0 points (-4.7 to -3.3) |
| 30 s | 5.2% | -10.2 points (-10.8 to -9.5) |
| 60 s | 0.4% | -14.9 points (-15.5 to -14.4) |

**H1:** supported in this model. A 30 s shift lowered simulated interaction probability from about 15% to about 5%.

**H2 (first look):** the effect is not proportional to the size of the shift. The first 5 s step changes probability by only 0.6 points, the 15-30 s steps each change it by roughly 2 points, and steps beyond 40 s change it by 1 point or less (see `marginal_effect.png`). This shape follows directly from the assumed travel-time distributions, so it shows the measurement works, not that real traffic behaves this way.

## Limitations

- Toy model: no road geometry, acceleration, right of way, signals or driver reactions.
- Conflict is approximated by arrival-time proximity, not true conflict-zone occupancy or TTC.
- Parameters are illustrative, not calibrated to NGSIM, INTERACTION or South African data.
- Results depend heavily on the 4 s window and the delay distribution (a sensitivity analysis is planned for Experiment 002).
- Simulated probabilities are not real-world crash probabilities.

## Next

Experiment 002: sensitivity analysis over conflict window, speed spread and delay spread.
