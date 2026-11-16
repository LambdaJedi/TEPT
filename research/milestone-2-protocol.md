# Milestone 2: dataset selection and experimental protocol (draft)

**Goal:** a documented specification that can be implemented in Python and SUMO without guessing at the data structure.

## Checklist

- [ ] Download NGSIM and INTERACTION samples; record fields, units, sampling frequency, licence.
- [ ] Choose one dataset for the first realistic experiment, with reasons.
- [ ] Define a traffic conflict mathematically (see candidate definition below).
- [ ] Decide trial count N from the target confidence-interval width.
- [ ] Write the baseline-versus-intervention protocol.
- [ ] Install SUMO and run a minimal two-vehicle TraCI example.

## Candidate conflict definition (to refine)

For vehicles i and j with trajectories X_i(t), X_j(t) and a conflict zone Z:

- Occupancy interval of vehicle i: [s_i, e_i], the times its body overlaps Z.
- **Conflict (Y = 1)** if [s_i, e_i] and [s_j, e_j] overlap.
- Also record: minimum separation, arrival-time difference |s_i - s_j|, and post-encroachment time PET = max(s_i, s_j) - min(e_i, e_j) when the intervals do not overlap.
- A "collision" is reserved for actual body overlap in space and time, never for close approaches.

## Candidate protocol

1. Fix network, routes, speeds and vehicle parameters.
2. Intervention: vehicle A departs at 08:00 (baseline), then 07:59, 07:58, 07:55, 08:05.
3. For each scenario run N trials, reusing the same random seeds across scenarios.
4. Record conflict, minimum separation and arrival-time difference per trial.
5. Report P_hat, ΔP against baseline, and intervals.
6. Compare the effect per unit of displacement across scenarios (H2).

## Choosing N

Binomial standard error is sqrt(p(1-p)/N). For p near 0.15, N = 20,000 gives a standard error of about 0.25 percentage points. Choose N so the interval is narrower than the smallest effect worth distinguishing.

## Open questions

1. NGSIM or INTERACTION?
2. Which conflict definition is the most defensible at intersections?
3. Can event-impact measures transfer to non-traffic events?
