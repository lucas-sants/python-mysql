#Data visualization in Python
#Scatterplot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7 , 1, 0]

title = "Scatterplot"
axisx = "Axis X"
axisy = "Axis Y" 

#Subtitles
plt.title(title)
plt.xlabel(axisx)
plt.ylabel(axisy)

plt.scatter(x, y, label = "My points", color = "r")
plt.plot(x,y)
plt.legend()

plt.show()