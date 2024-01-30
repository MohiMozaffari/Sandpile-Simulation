# Sandpile Simulation

Author: [Author's Name]
Affiliation: [Author's Affiliation]

## Introduction

This repository contains Python code for simulating sandpile dynamics on a square lattice using a probabilistic cellular automaton model. Sandpile models are often used to study self-organized criticality, a property of dynamic systems that exhibit scale-invariance and power-law distributions.

## Getting Started

To run the simulation, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running:
```bash
pip install numpy matplotlib seaborn
```
4. Run the script `sandpile_simulation.py`:

```bash
python sandpile_simulation.py
```
## Code Structure
The code consists of the following main parts:

* addsand(lattice): Adds a grain of sand to a randomly chosen site on the lattice.
* check(lattice): Checks the stability of the lattice and triggers avalanches if any site has reached a critical state.
* simulate(lattice, i): Simulates the sandpile dynamics for a specified number of iterations.
* CountFrequency(my_list): Counts the frequency of avalanche sizes.
* ine(x,a,b): Defines a linear function for curve fitting.
## Parameters
* N: Size of the lattice.
* nstep: Number of iterations for the simulation.
## Visualization
The simulation results are visualized using Seaborn's heatmap, showing the sandpile configuration after the specified number of iterations. Additionally, the frequency of avalanche sizes is plotted on a log-log scale, and a linear fit is applied to estimate the slope (tau) of the power-law distribution.

## Output
The simulation generates two plots:

* Heatmap showing the sandpile configuration after the simulation.
* Log-log plot of avalanche size frequency with the estimated value of tau.
