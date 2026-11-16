# Candidate datasets

Each serves a different purpose. Do not combine them indiscriminately. Inspect fields, licensing and sampling frequency before relying on any of them (Milestone 2).

| Dataset | What it offers | Notes |
| --- | --- | --- |
| NGSIM | Vehicle positions about every 0.1 s, with speed, acceleration, lane and vehicle info | Strong first candidate for trajectory behaviour and driver-model calibration. https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj/data |
| INTERACTION | Interactive scenarios: intersections, merging, lane changes, near-collisions; vehicle and pedestrian trajectories, semantic maps | Strong candidate for intersections. https://huggingface.co/datasets/INTERACTION-dataset/INTERACTION-dataset |
| highD | More than 110,000 vehicle trajectories from six German highway locations | Academic/non-commercial access conditions apply. https://ika.rwth-aachen.de/en/competences/projects/automated-driving/highd-dataset.html |
| Cape Town accidents 2019-2024 | 377,996 police-attended accidents | Local context only. Inspect fields and licensing first. https://portal.transport-data.org/@tumi/traffic-accidents-cape-town-south-africa-2019-2024 |
| NHTSA FARS / CRSS | US fatal crash census / sampled police-reported crashes | No continuous trajectories. |

## Limitations to keep in mind

- South African RTMC crash records are not continuous vehicle-trajectory data, and the underlying RTMC data has reportedly required a formal agreement to access.
- A model calibrated on German or American roads is not validated for South African driving conditions.

## Recommendation

Use NGSIM or INTERACTION for the first trajectory experiment. Keep South African crash statistics as a separate local-context research stream.
