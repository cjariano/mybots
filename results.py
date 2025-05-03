import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read in results
with open("log_quadruped_fitness.txt", 'r') as file:
    lines = file.readlines()
    quadruped_vals = [float(line.strip()) for line in lines if line.strip()]

with open("log_hexapod_fitness.txt", 'r') as file:
    lines = file.readlines()
    hexapod_vals = [float(line.strip()) for line in lines if line.strip()]

# Take absolute values
quadruped_vals = np.abs(quadruped_vals)
hexapod_vals = np.abs(hexapod_vals)

# Calculate averages
quadruped_avg = np.mean(quadruped_vals)
hexapod_avg = np.mean(hexapod_vals)

print(f"quadruped average: {quadruped_avg}\nhexapod average: {hexapod_avg}")
print(f"quadruped max: {np.max(quadruped_vals)}\nhexapod max: {np.max(hexapod_vals)}")

# First graph
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(quadruped_vals, label='Quadruped')
plt.plot(hexapod_vals, label='Hexapod')
plt.xlabel('Robot')
plt.ylabel('Fitness in -x direction')
plt.title('Fitness values of Robots')
plt.legend()

# Second graph - sorted bar chart
# Sort both lists descending
sorted_quad = sorted(quadruped_vals, reverse=True)
sorted_hexa = sorted(hexapod_vals, reverse=True)

# Make sure they are the same length
min_len = min(len(sorted_quad), len(sorted_hexa))
sorted_quad = sorted_quad[:min_len]
sorted_hexa = sorted_hexa[:min_len]

# Indices for grouped bars
x = np.arange(min_len)
width = 0.35

plt.subplot(1, 2, 2)
plt.bar(x - width/2, sorted_quad, width, label='Quadruped')
plt.bar(x + width/2, sorted_hexa, width, label='Hexapod')
plt.xlabel('Ranked Index')
plt.ylabel('Fitness in -x direction')
plt.title('Sorted Fitness Values (High to Low)')
plt.legend()

plt.tight_layout()
plt.show()
