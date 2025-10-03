#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

#Parabola
t1 = np.linspace(-6,6,1000)
x_p = 2*t1*t1
y_p = 4*t1

#Circle
t2 = np.linspace(0, 2*np.pi, 1000)
x_c = 1 + np.sqrt(5)*np.cos(t2)
y_c = 2 + np.sqrt(5)*np.sin(t2)

#Lines
x_1 = np.linspace(0,2, 1000)
y_1 = 2*x_1

x_2 = np.linspace(0,2, 1000)
y_2 = 0*t1

x_3 = 2*t1/t1
y_3 = np.linspace(0, 4, 1000)


fig, ax = plt.subplots()

#Labelling
ax.set_title("Solution Image")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

#Plotting Curves and Lines
ax.plot(x_c, y_c, c="r", label="Circle")
ax.plot(x_p, y_p, c="b", label="Parabola")
ax.plot(x_1,y_1, c="g", ls="--", label="Triangle PQS")
ax.plot(x_2,y_2, c="g", ls="--")
ax.plot(x_3,y_3, c="g", ls="--")

#Plotting and Labelling Points
ax.scatter(0,0, c="g", s=50, zorder=5, marker="8", edgecolor="k")
ax.text(0,0, "P(0,0)", fontsize=10, fontweight="bold", ha="right", va="top")
ax.scatter(2,0, c="#FF00FF", s=50, zorder=5, marker="8", edgecolor="k")
ax.text(2.1,-.2, "S(2,0)", fontsize=10, fontweight="bold")
ax.scatter(2,4, c="g", s=50, zorder=5, marker="8", edgecolor="k")
ax.text(2.1,3.9, "Q(2,4)", fontsize=10, fontweight="bold")

#Shading Area of Triangle PQS
poly = Polygon([[0,0],[2,0],[2,4]], closed=True, facecolor="#41dc8e", alpha=0.4)
ax.add_patch(poly);

#Anonymous Atributes
ax.set_aspect("equal")
ax.grid(True)
ax.legend(loc="best")

#Adjusting the Axises
ax.set_xticks(np.arange(-3,6, 1))
ax.set_yticks(np.arange(-3,6, 1))
ax.set_xlim(-3, 5)
ax.set_ylim(-3, 5)

plt.savefig("fig.png", dpi=300)

print("Area Of Triangle PQS is: 4 sq.units")
