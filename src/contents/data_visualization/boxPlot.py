#BoxPlot - Box Diagram

import matplotlib.pyplot as plt
import random

vector = []

for i in range(10):
	random_number = random.randint(0,5)
	vector.append(random_number)

plt.boxplot(vector)
plt.title("Boxplot")
plt.show()