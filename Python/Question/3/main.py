#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

print("Finding Points of Intersections between (x-1)^2 + (y-3)^2 = r^2 and (x-4)^2 + (y+1)^2 = 9\n")

r = abs(float(input("Enter value of r: ")))

t = np.linspace(0,2*np.pi, 100000)

#Circle-1: (x-1)^2 + (y-3)^2 = r^2
x1 = 1 + r*np.cos(t)
y1 = 3 + r*np.sin(t)

#Circle-2: (x-4)^2 + (y+1)^2 = 9
x2 = 4 + 3*np.cos(t)
y2 = -1 + 3*np.sin(t)



#POI OF THE CIRCLES
D = np.sqrt(-(r**4) + 68*(r*r) -256)
x_p1 = (3*r*r + 98 + 4*D)/50
y_p1= (86 - 4*r*r + 3*D)/50

x_p2 = (3*r*r + 98 - 4*D)/50
y_p2= (86 - 4*r*r - 3*D)/50


fig, ax = plt.subplots()

#Setting Title and labelling Axises
ax.set_title("Point of Intersection of Circles", fontweight="bold")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

#Plotting Circles
ax.plot(x1,y1, c="b", label=f"$(x-1)^2 + (y-3)^2 = r^2$")
ax.plot(x2, y2, c="g", label=f"$(x-4)^2 + (y+1)^2$ = 9")

#Plotting and Labelling Center of Circles
ax.scatter(1,3, c="r", label=f"$C_1$(1,3)", edgecolor="k", s=50, marker="8")
ax.text(1,3, f"$C_1$")
ax.scatter(4,-1, c="r", label=f"$C_2$(4,-1)", edgecolor="k", s=50, marker="8")
ax.text(4,-1, f"$C_2$")

#Plotting and Labelling Points of Intersections
if x_p1 != x_p2:
    ax.scatter(x_p1, y_p1, c="#FF00FF", label=f"P({x_p1:.2f}, {y_p1:.2f})", s=50, edgecolor="k", zorder=5, marker="*")
    ax.text(x_p1, y_p1, f"P({x_p1:.2f}, {y_p1:.2f})",fontsize=11, fontweight="bold", ha="left", va="top")
    ax.scatter(x_p2, y_p2, c="#FF00FF", label=f"Q({x_p2:.2f}, {y_p2:.2f})", s=50, edgecolor="k", zorder=6, marker="*")
    ax.text(x_p2, y_p2, f"Q({x_p2:.2f}, {y_p2:.2f})",fontsize=11, fontweight="bold", ha="center", va="top")

else:
    ax.scatter(x_p1, y_p1, c="#FF00FF", label=f"R({x_p1:.2f}, {y_p1:.2f})", s=50, edgecolor="k", zorder=5, marker="*")
    ax.text(x_p1, y_p1, f"R({x_p1:.2f}, {y_p1:.2f})",fontsize=11, fontweight="bold", ha="left", va="top")


#Anonymous Atributes
ax.legend(loc="best")
ax.grid(True)
ax.set_aspect("equal")

#Displaying the Image
plt.show()
