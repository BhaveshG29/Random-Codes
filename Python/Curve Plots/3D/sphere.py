#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

h, k, l, r = map(float, input("Enter h k l r: ").split())

u = np.linspace(0.0, 2.0 * np.pi, 100)
v = np.linspace(0.0, np.pi, 100)
u, v = np.meshgrid(u, v)

x = h + r * np.cos(u) * np.sin(v)
y = k + r * np.sin(u) * np.sin(v)
z = l + r * np.cos(v)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, z, color="r", alpha=0.6, edgecolor="none")

max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max()
mid_x = (x.max() + x.min()) * 0.5
mid_y = (y.max() + y.min()) * 0.5
mid_z = (z.max() + z.min()) * 0.5
ax.set_xlim(mid_x - 0.5*max_range, mid_x + 0.5*max_range)
ax.set_ylim(mid_y - 0.5*max_range, mid_y + 0.5*max_range)
ax.set_zlim(mid_z - 0.5*max_range, mid_z + 0.5*max_range)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Sphere")
ax.set_aspect("equal")

plt.tight_layout()
plt.savefig("figs/Sphere.png")
plt.show()


