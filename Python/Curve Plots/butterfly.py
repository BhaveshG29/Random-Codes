#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 10000)
x = np.sin(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - np.power(np.sin(t/12), 5))
y = np.cos(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - np.power(np.sin(t/12), 5))


fig, ax= plt.subplots()
ax.set_title("Butterfly")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.plot(x, y, c="r", label="Butterfly")
ax.scatter(0,0, c="b", edgecolor="k", marker="8", zorder=5, s=90, label="Origin")

ax.grid(True)
ax.legend(loc="best")
ax.set_aspect("equal")

plt.savefig("figs/Butterfly.png", dpi=300)
plt.show()

