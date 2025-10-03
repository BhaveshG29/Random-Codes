#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

#x^(2/3) + y^(2/3) = a^(2/3)
print("x^(2/3) + y^(2/3) = a^(2/3)\n\n")

a = float(input("Enter the value of a:"))

t = np.linspace(0,2.0001, 100)
x = a*np.power(t/2, 3/2)
y = a*np.power((1-t/2), 3/2)

fig, ax = plt.subplots()

ax.set_title("Astroid")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.plot(x,y, c="r", label="Astroid")
ax.plot(x,-y, c="r")
ax.plot(-x,y, c="r")
ax.plot(-x,-y, c="r")

ax.set_aspect("equal")
ax.grid(True)
ax.legend(loc="best")

plt.savefig("figs/astroid.png", dpi=300)
plt.show()
