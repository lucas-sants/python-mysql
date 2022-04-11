# Data visualization in Python

import matplotlib.pyplot as plt

#First example basic
x = [1, 2]
y = [2, 3]

plt.plot(x, y)
plt.show()

#Graphic with subtitle

#Title
plt.title("My first Graphic with Python")

#Axis
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x, y)
plt.show()