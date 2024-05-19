# importing the necessary libraries for the project
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, solve

# Define the range for the ratio of lengths (L3/L1)
r = np.arange(-5, 5, 0.001)

# Constants
a = 3 * (4**(1/3) - 1)
b = 1/4
c = 1/4**(1/3)
p = a * b
q = a * c

# Dimensionless power (P*)
dim_p = (p / (r - 1)) - ((r * q) / (r - 1))

# Plotting the values of the dimensionless power
plt.figure()
plt.plot(r, dim_p, 'r-', linewidth=1)
plt.grid(True)
plt.title('Dimensionless Power Vs Length Ratio')
plt.xlabel('r', fontweight='bold', fontsize=11)
plt.ylabel('p*', fontweight='bold', fontsize=11)
plt.gca().get_xaxis().set_tick_params(direction='out', width=2)
plt.gca().get_yaxis().set_tick_params(direction='out', width=2)
plt.show()

# Solving for the max value
# Computing the maximum dimensionless power
r_sym = symbols('r')
dim_pr = (p / (r_sym - 1)) - ((r_sym * q) / (r_sym - 1))