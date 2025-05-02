import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# read in results into lists
with open("log_quadruped_fitness.txt", 'r') as file:
    lines = file.readlines()
    quadruped_vals = [float(line.strip()) for line in lines if line.strip()]


quadruped_avg = sum(quadruped_vals)/len(quadruped_vals)

with open("log_hexapod_fitness.txt", 'r') as file:
    lines = file.readlines()
    hexapod_vals = [float(line.strip()) for line in lines if line.strip()]


hexapod_avg = sum(hexapod_vals)/len(hexapod_vals)



print(f"quadruped average: {quadruped_avg}\nhexapod average: {hexapod_avg}")
print(f"quadruped max: {min(quadruped_vals)}\nhexapod max: {min(hexapod_vals)}")


plt.plot(np.abs(quadruped_vals), label = 'Quadruped')
plt.plot(np.abs(hexapod_vals), label = 'Hexapod')


plt.xlabel('Robot')
plt.ylabel('Fitness in -x direction')
plt.title('Fitness values of Robots')
plt.xticks(range(20), labels = range(1,21))
plt.legend()

results = pd.DataFrame({'Quadruped': quadruped_vals,
                        'Hexapod': hexapod_vals})

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
