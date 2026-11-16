I've started an independent research and software engineering project exploring how small changes in timing can influence interconnected events.

Experiment 001 is deliberately simple: two vehicles approach a shared intersection, and I change one vehicle's departure time. Across 20,000 simulated trips per scenario, delaying it by 30 seconds lowered the simulated interaction probability from about 15% to about 5%, and each extra few seconds did not have an equal effect.

This is a toy model with illustrative parameters, so it demonstrates the method rather than describing real traffic. Next I'll test how sensitive the result is to my assumptions, then move to real trajectory data.

Code, graphs and limitations are on GitHub: [link]

Feedback and challenges welcome.

#Python #Simulation #MonteCarlo #SoftwareEngineering
