#Data visualization in Python
#Save the figure

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7 , 1, 0]
z = [200, 5, 400, 3300, 10]

title = "Scatterplot"
axisx = "Axis X"
axisy = "Axis Y" 

#Subtitles
plt.title(title)
plt.xlabel(axisx)
plt.ylabel(axisy)

plt.plot(x,y,color="k",linestyle="--")
plt.scatter(x, y, label = "My points", color = "#990000", marker=".", s=z)
plt.legend()

#plt.show()

"""
Methods to save a figure
"""
#plt.savefig("figure1.png")
#plt.savefig("figure1.pdf")

#plt.savefig("figure1.png", dpi=300)