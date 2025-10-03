#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

#Setting Mathematical Conditions
t = np.linspace(0,2*np.pi, 10000)
x = np.sin(3*t + np.pi/4)
y = np.sin(2*t)


fig, ax = plt.subplots()

#Plotting the Curve
ax.plot(x,y, c="r", label="Curve")

#Adding Labels
ax.set_title("Lissajous curve")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

#Anonymous Attributes
ax.grid(True)
ax.set_aspect("equal")

#Adjusting the Axises
ax.set_xticks(np.arange(-1,1.01, 0.5))
ax.set_yticks(np.arange(-1,1.01,0.5))

#Labelling Self Point of Intersection
ax.scatter(0, -0.5, c="g", marker="8", zorder=5, edgecolor="k", s=90, label="SPOI")
ax.text(0,-0.55, "P(0,-0.5)",  fontsize=10, fontweight="bold", ha="center", va="top")

#Adding Legend
ax.legend(loc="best")

plt.show()
