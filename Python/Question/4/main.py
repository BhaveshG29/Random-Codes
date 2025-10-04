#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

#Ellipse
t = np.linspace(0, 2*np.pi, 100000)
x_e = np.sqrt(2)*np.cos(t)
y_e = np.sin(t)

#Locus Of Mid-point: x^2 + 2y^2 = 4x^2y^2
x = np.linspace(-10*np.sqrt(2), 10*np.sqrt(2), 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)
Z = (X*X) + 2*(Y*Y) - 4*(X*X)*(Y*Y)



fig, ax = plt.subplots()

#Setting Title and Labelling Axises
ax.set_title("Solution Image")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

#Plotting Ellipse and Locus
ax.plot(x_e, y_e, c="r", label="Ellipse")
ax.contour(X, Y, Z, colors="b")

#Adjusting Axises
ax.set_xlim(-6, 6)
ax.set_ylim(-4, 4)

#Plotting Points of Intersection
ax.scatter(1, 1/np.sqrt(2), c="g", zorder=5, edgecolor="k", marker="8", label="Point of Intersections", s=20)
ax.scatter(1, -1/np.sqrt(2), c="g", zorder=5, edgecolor="k", marker="8", s=20)
ax.scatter(-1, 1/np.sqrt(2), c="g", zorder=5, edgecolor="k", marker="8", s=20)
ax.scatter(-1, -1/np.sqrt(2), c="g", zorder=5, edgecolor="k", marker="8", s=20)

#Anonymous Attributes
ax.plot([], [], color='b', label="Locus Of Mid-point")
ax.legend(loc="best")
ax.grid(True)
ax.set_aspect("equal")

#Saving and Showing the Image
plt.tight_layout()
plt.savefig("solution.png", dpi=300)
plt.show()
