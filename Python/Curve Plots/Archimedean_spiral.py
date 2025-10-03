#CODE BY BHAVESH G


import numpy as np
import matplotlib.pyplot as plt

print("Consider Polar Coordinate as:\t r= a + bθ\n")

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

t = np.linspace(0, 2*np.pi, 100000)
r = a + b*t
x = r*np.cos(t)
y = r*np.sin(t)


axis = np.linspace(-10*abs(b)-abs(a),10*abs(b)+abs(a), 10000) 

fig, ax = plt.subplots()

ax.set_title("Archimedean Spiral")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.plot(x,y, c="r", label="Curve")
ax.scatter(a,0, c="b", marker="8", label="Starting Point", edgecolor="k", zorder=5, s=20)
ax.plot(axis,0*axis, c="#000")
ax.plot(axis*0, axis, c="#000")


ax.set_aspect("equal")
ax.legend(loc="best")
ax.grid(True)
ax.set_xlim(-10*abs(b)-abs(a),10*abs(b)+abs(a),)
ax.set_ylim(-10*abs(b)-abs(a),10*abs(b)+abs(a),)

plt.tight_layout()
plt.savefig("figs/Archimedean_spiral.png", dpi=300)
plt.show()

