#CODE BY BHAVESH G

#Plotting y^3 = ax^2

import numpy as np
import matplotlib.pyplot as plt

print("Plotting y^3 = ax^2.\n\n")

a = float(input("Enter the Value of a:"))

t = np.linspace(-10000, 10000, 99999)

# Parametric Coordinates: y= (t^2)a^(1/3) & x = t^3

y = np.power(a, 1/3)*abs(t*t)
x = np.power(t, 3)

fig, ax = plt.subplots()
ax.plot(x,y, c="r", ls="--")
ax.set_title("y^3 = ax^2")
ax.scatter(0,0, c="b", marker="*")
ax.set_xlim(-100*a,100*a)
ax.set_ylim(-100*a,100*a)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_aspect("equal")

plt.show()

