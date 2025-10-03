#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

print("Hypotrochoid")
R = float(input("Enter value of radius of Fixed circle: "))
r = float(input("Enter value of radius of Rotating circle: "))
d = float(input("Enter value of distance of generating point: "))


t = np.linspace(0, 6*np.pi, 50000)
x = (R-r)*np.cos(t) + d*np.cos(((R-r)/r)*t)
y = (R-r)*np.sin(t) - d*np.sin(((R-r)/r)*t)
 
fig, ax = plt.subplots()

ax.set_title("Hypotrochoid")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.plot(x,y, c="r", label="Hypotrochoid")


ax.set_aspect("equal")
ax.legend(loc="best")
ax.grid(True)

plt.savefig("figs/Hypotrochoid.png", dpi=300)
plt.show()
