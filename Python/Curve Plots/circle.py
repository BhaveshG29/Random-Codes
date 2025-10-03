#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt


x_0 = float(input("Enter the X-coordinate of the circle:"))
y_0 = float(input("Enter the Y-coordinate of the circle:"))
R = float(input("Enter the radius of the circle:"))

t = np.linspace(0,2*np.pi, 2000)

x = x_0 + R*np.cos(t)
y = y_0 + R*np.sin(t)


fig, ax = plt.subplots()

ax.plot(x,y, c="r")

ax.set_title("Circle")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_aspect("equal")
ax.scatter(x_0,y_0, c="b")
ax.text(x_0, y_0, f'C ({x_0:.2f}, {y_0:.2f})', ha='left', va='bottom', fontsize=7)
plt.savefig("figs/circle.png", dpi=300)
plt.show()

