# Logistic Growth Model

This repository contains a Python implementation of the logistic growth model, a common model in population dynamics.

## Description
The logistic growth equation models population growth with a carrying capacity:

$$
\frac{dP}{dt} = kP (M - P)
$$


where:
- \( P \) is the population size,
- \( k \) is the growth rate,
- \( M \) is the carrying capacity,
- \( t \) is time.

The program numerically solves this equation using Python's `scipy.integrate.solve_ivp` and visualizes the population growth.

## Installation
To run the script, ensure you have Python installed along with the required libraries:

```sh
pip install numpy matplotlib scipy
```

## Usage
Run the Python script:

```sh
python LogisticGrowthModel.py
```

This will generate a plot showing how the population grows over time and approaches the carrying capacity.

## Output
The program outputs a graph of population vs. time, showing logistic growth behavior.

## License
This project is licensed under the MIT License.

