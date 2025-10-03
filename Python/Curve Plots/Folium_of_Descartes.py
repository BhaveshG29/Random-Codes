#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

#x^3 + y^3 = 3axy
print("Equation of Folium of Descartes:\t x^3 + y^3 = 3axy\n\n")

a = float(input("Enter the value of a:"))


eps = 1e-6
N = 20000
t1 = np.linspace(-10, -1 - eps, N//2)
t2 = np.linspace(-1 + eps,  10,   N//2)

x1 = 3*a*t1/(1 + t1*t1*t1)
y1 = 3*a*t1*t1/(1 + t1*t1*t1)

x2 = 3*a*t2/(1 + t2*t2*t2)
y2 = 3*a*t2*t2/(1 + t2*t2*t2)


lim = 5*a
m1 = np.isfinite(x1) & np.isfinite(y1) & (np.abs(x1) < lim) & (np.abs(y1) < lim)
m2 = np.isfinite(x2) & np.isfinite(y2) & (np.abs(x2) < lim) & (np.abs(y2) < lim)

fig, ax = plt.subplots()
ax.set_title("Folium of Descartes")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.plot(x1[m1], y1[m1], c="r", label="Curve")
ax.plot(x2[m2], y2[m2], c="r")

ax.scatter(0, 0, c="b", s=50, zorder=5, edgecolor="k", label="SPOI")
ax.grid(True)
ax.legend()
ax.set_aspect("equal")


ax.set_xlim(-a*2, a*2)
ax.set_ylim(-a*2, a*2)

plt.savefig("figs/Folium_of_Descartes.png", dpi=300)
plt.show()
