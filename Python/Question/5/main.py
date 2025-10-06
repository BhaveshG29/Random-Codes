#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

#4x^2 + 9y^2 = 1
#Given Line: 8x=9y

#Tangent Equations: 8x = 9y - 5 & 8x = 9y + 5

#Ellipse:
t = np.linspace(0, 2*np.pi, 100000)
x_e = np.cos(t)/2
y_e = np.sin(t)/3



#Tangent Lines:
X = np.linspace(-1, 1, 100000)
Y1 = (8*X + 5)/9
Y2 = (8*X - 5)/9

fig, ax = plt.subplots()

#Setting Title and Labelling Axises
ax.set_title("Solution")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.plot(x_e, y_e, c="b", label = f"$4x^2 + 9y^2 = 1$")
ax.plot(X, Y1, c="r", label="Tangent-1" )
ax.plot(X, Y2, c="g", label="Tangent-2")

ax.scatter(-0.4, 0.2, c="r", marker="8", edgecolor="k", zorder=5, label=f"$q_1$")
ax.text(-0.4, 0.2, f"$q_1$(-0.4,0.2)", ha="left", va="top", fontweight="bold")
ax.scatter(0.4, -0.2, c="g", marker="8", edgecolor="k", zorder=5, label=f"$q_2$")
ax.text(0.4, -0.2, f"$q_1$(0.4,-0.2)", ha="left", va="top", fontweight="bold")

ax.set_xlim(-0.75, 0.75)
ax.set_ylim(-0.75, 0.75)

ax.set_aspect("equal")
ax.grid(True)
ax.legend(loc="best")

plt.tight_layout()
plt.savefig("Solution.png", dpi=300)
plt.show()
