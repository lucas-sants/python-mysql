# Data visualization in Python
# Bar Graph

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7 , 1, 0]

title = "Bar Graph"
axisx = "Axis X"
axisy = "Axis Y" 

#Subtitles
plt.title(title)
plt.xlabel(axisx)
plt.ylabel(axisy)

plt.bar(x, y)
plt.show()