#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

#Setting Mathematical Foundation
x = np.linspace(0,2*np.pi, 10000)
y1 = np.sin(x) 
y2 = np.cos(x)

x_ticks = np.arange(0, 2*np.pi, np.pi/4)

fig, ax = plt.subplots()

#Labeling Axises and Setting a Title
ax.set_title("Sine and Cosine Graph")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

#Plotting sine and cosine graphs
ax.plot(x, y1, c="r", label = "y = sin(x)")
ax.plot(x, y2, c="b", label = "y = cos(x)")

#Adding Legend
ax.legend()

ax.set_aspect("equal")

#Adjusting the Axises
ax.set_xticks(x_ticks)
ax.set_xlim(-0.1, 2*np.pi+0.1)
ax.set_ylim(-1.1, 1.1)
ax.grid(True)

#Showing Point of Intersecting between graphs
ax.scatter(np.pi/4, 1/np.power(2, 1/2), c="g", zorder=5)
ax.scatter(5*np.pi/4, -1/np.power(2, 1/2), c="g", zorder=5)


plt.show()

