import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# read in results into lists
with open("log_quadruped_fitness.txt", 'r') as file:
    lines = file.readlines()
    quadruped_vals = [float(line.strip()) for line in lines if line.strip()]


quadruped_avg = sum(quadruped_vals)/len(quadruped_vals)

with open("log_hexapod1_fitness.txt", 'r') as file:
    lines = file.readlines()
    hexapod1_vals = [float(line.strip()) for line in lines if line.strip()]


hexapod1_avg = sum(hexapod1_vals)/len(hexapod1_vals)

with open("log_hexapod2_fitness.txt", 'r') as file:
    lines = file.readlines()
    hexapod2_vals = [float(line.strip()) for line in lines if line.strip()]


hexapod2_avg = sum(hexapod2_vals)/len(hexapod2_vals)

print(f"quadruped average: {quadruped_avg}\nhexapod 1 average: {hexapod1_avg}\nhexapod 2 average: {hexapod2_avg}")
print(f"quadruped max: {min(quadruped_vals)}\nhexapod 1 max: {min(hexapod1_vals)}\nhexapod 2 max: {min(hexapod2_vals)}")


plt.plot(np.abs(quadruped_vals), label = 'Quadruped')
plt.plot(np.abs(hexapod1_vals), label = 'Hexapod 1')
plt.plot(np.abs(hexapod2_vals), label = 'Hexapod 2')

plt.xlabel('Robot')
plt.ylabel('Fitness in -x direction')
plt.title('Fitness values of Robots')
plt.xticks(range(20), labels = range(1,21))
plt.legend()

results = pd.DataFrame({'Quadruped': quadruped_vals,
                        'Hexapod 1': hexapod1_vals,
                        'Hexapod 2': hexapod2_vals})

print(results)

results_long = (
    results
    .melt(var_name = 'robot', value_name = 'fitness')
)

results_long['fitness'] = np.abs(results_long['fitness'])

results_grid = sns.FacetGrid(
    data = results_long,
    col = 'robot',
    sharex = False,

)

results_grid.map(sns.histplot, 'fitness')

plt.show()
