# TEPT hypotheses (specification v0.1)

TEPT is a provisional name for a research programme, not an established theory. Its contribution must be demonstrated against existing methods.

## Working research question

> Can small changes in the timing or occurrence of an event measurably alter the probability of downstream events in an interconnected system, and can events with disproportionately large downstream effects be identified?

## Hypotheses

**H1: Temporal sensitivity.** Changing an agent's departure time, holding other model inputs constant, can change the probability of a later interaction or conflict.
*Status:* supported in the Experiment 001 toy model.

**H2: Unequal propagation.** The downstream effect of a small temporal change is not always proportional to the size of the change. Some interventions may produce substantially larger changes than others.
*Status:* first indication in Experiment 001 (marginal effect per 5 s step varies from 0.2 to 2.3 points). Not yet tested on realistic networks.

**H3: Identifiable high-impact events.** Within a defined simulation and set of assumptions, interventions can be ranked by their estimated effect on a selected downstream outcome, with uncertainty reported.
*Status:* not yet tested.

## What TEPT must distinguish itself from

| Existing field | What it already studies | What TEPT investigates |
| --- | --- | --- |
| Temporal networks | Connections between entities that change over time | Whether small timing changes alter later network interactions and outcomes |
| Causal inference | Whether an intervention changes an outcome | How an intervention's effects propagate through a sequence of events |
| Counterfactual modelling | What might have happened under a different action | How alternative event sequences diverge from a baseline |
| Agent-based modelling | How agents interact under rules | How temporal changes in individual agents affect system-level outcomes |
| Monte Carlo methods | Distributions of outcomes over repeated random runs | The distribution of downstream effects across alternative timelines |

The claim "small events affect the future" is already familiar in complex systems and is not the contribution. The question worth testing is whether the propagation of an intervention through a time-dependent interaction network can be defined and measured, and whether interventions with unusually large downstream effects can be identified relative to comparable changes.

## Unresolved questions

1. Which dataset gives the best first realistic experiment: NGSIM or INTERACTION?
2. How should a traffic conflict be defined consistently?
3. How many trials give sufficiently precise probability estimates?
4. Can the same measures be applied meaningfully to non-traffic events?
