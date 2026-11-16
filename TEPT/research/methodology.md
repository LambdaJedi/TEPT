# TEPT methodology (specification v0.1)

## Variables

| Symbol | Meaning | Type |
| --- | --- | --- |
| T_i | Agent i's departure time | Input |
| R_i | Agent i's route | Input |
| V_i(t) | Agent i's speed over time | Dynamic |
| X_i(t) | Agent i's position over time | Dynamic |
| E(t) | Environmental conditions | Context |
| I_ij | Interaction between agents i and j | Event |
| C | Defined traffic conflict or collision event | Outcome |
| Y | Selected downstream outcome | Outcome |

## Intervention and outcome

Let `a` be an intervention, for example shifting a vehicle's departure from 08:00 to 07:58. Y = 1 means two vehicles enter a defined conflict zone within a specified time window.

Outcome probability under an intervention: P(Y = 1 | do(a)).

Effect relative to baseline: ΔP_Y = P(Y = 1 | do(a1)) - P(Y = 1 | do(a0)).

Monte Carlo estimate over N trials: P_hat(Y = 1 | do(a)) = (number of trials with Y_k = 1) / N.

This is a simulated estimate, not a real-world crash probability. Its quality depends on the realism and calibration of the simulation.

## Experimental design rules

1. Use the same random seeds and matched traffic conditions for baseline and intervention runs (common random numbers). Experiment 001 does this.
2. Change one thing at a time (initially departure time only).
3. Report every estimate with an uncertainty interval.
4. Do not call every close approach a collision. Define a conflict from measurable conditions such as overlapping occupancy of a shared conflict zone.
5. Choose N so the confidence interval half-width is small relative to the effect being compared (binomial standard error is sqrt(p(1-p)/N)).

## Metrics (reported separately; no composite score yet)

1. **Temporal displacement:** TD = |T_1 - T_0|.
2. **Outcome probability difference:** ΔP_Y = P_hat_1(Y) - P_hat_0(Y).
3. **Propagation depth:** number of downstream event stages reached from the intervention in the event graph.
4. **Propagation breadth:** number of distinct downstream events or agents affected.
5. **Uncertainty:** confidence or simulation-based intervals around estimated effects.

A single combined "Event Impact Score" is postponed. Combining probability change, depth and breadth risks hiding important differences, so a composite is only justified if there is a clear scientific reason.

## Physical measures (for later experiments)

Time to collision: TTC = d / v_closing, where d is the gap and v_closing the positive relative closing speed.

Stopping distance: d_stop = v * t_r + v^2 / (2a), with reaction time t_r and braking deceleration magnitude a.

These are longitudinal simplifications. At intersections, use trajectory geometry, conflict-zone occupancy and vehicle dimensions.

## Causal inference caveat

A driver leaving earlier and avoiding a conflict in one simulation does not show that leaving earlier caused the difference in the real world. Counterfactual comparisons need explicit assumptions, controlled variables and well-defined interventions.

## Tooling decisions

| Decision | Initial choice |
| --- | --- |
| Language | Python |
| Traffic simulator | SUMO (Eclipse) |
| Simulator interface | TraCI |
| Analysis | pandas, NumPy, SciPy |
| Event graph | NetworkX |
| Dashboard | Streamlit |
| First data candidate | NGSIM |
| Alternative | INTERACTION |
| Initial intervention | Departure-time displacement |
| Initial outcome | Defined vehicle conflict |
| Probability method | Repeated Monte Carlo simulation |

No machine learning or LLM is needed for the first experiments.
