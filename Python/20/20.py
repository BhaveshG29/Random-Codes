#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt("x.dat", delimiter=",")
y = np.genfromtxt("y.dat", delimiter=",")

plt.plot(x,y, c="r", label="Parabola")
plt.plot(-x, y, c="r")


plt.grid(True)
plt.legend(loc="upper right")

plt.show()
