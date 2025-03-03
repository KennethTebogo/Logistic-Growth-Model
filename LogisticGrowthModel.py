import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def logistic_growth(t, P, k, M):
    return k * P * (M - P)

# Parameters
k = 0.03  # Growth rate
M = 100  # Carrying capacity
P0 = 10  # Initial population

time_span = (0, 100)  # Time range for simulation
time_eval = np.linspace(0, 100, 1000)  # Time points to evaluate the solution

# Solve the differential equation
solution = solve_ivp(logistic_growth, time_span, [P0], args=(k, M), t_eval=time_eval)

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(solution.t, solution.y[0], label=f"P0 = {P0}", color='b')
plt.axhline(y=M, color='r', linestyle='--', label=f"Equilibrium P = {M}")
plt.xlabel("Time (t)")
plt.ylabel("Population (P)")
plt.title("Logistic Growth Model")
plt.legend()
plt.grid()
plt.show()

