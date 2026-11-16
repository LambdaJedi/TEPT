# TEPT

A research-driven software engineering project investigating whether small changes in the timing of events measurably alter downstream outcomes in interconnected systems. TEPT is a provisional name for a research programme, not an established theory. The first domain is road traffic because vehicle movements are measurable.

**Working question:** Can small changes in the timing or occurrence of an event measurably alter the probability of downstream events, and can events with disproportionately large downstream effects be identified?

## Status

| Milestone | State |
| --- | --- |
| 1. Research specification v0.1 | Done (`research/`) |
| Experiment 001: departure timing, two vehicles | Done (`experiments/experiment-001/`) |
| 2. Dataset selection and experimental protocol | Draft (`research/milestone-2-protocol.md`) |

## Headline result so far

In a toy Monte Carlo model, delaying one of two vehicles by 30 s lowered simulated interaction probability from 15.4% to 5.2%, and the effect of each extra 5 s was not constant. This is a proof of method, not a real-world finding. See the experiment README for limitations.

## Layout

```
TEPT/
├── experiments/experiment-001/   simulation, results, README
├── research/                     hypotheses, methodology, datasets, milestone 2
├── applications/                 butterfly-project, predictive-road-safety (planned)
├── requirements.txt
└── README.md
```

## Quick start

```
pip install -r requirements.txt
cd experiments/experiment-001
python simulation.py
```

## Workflow

Each experiment ends with a commit, a graph, an honest write-up of what was and was not established, and optionally a short post.
