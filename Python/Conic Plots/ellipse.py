#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt

print("Considering Equation of Ellipse as: (x-h)^2/a^2 + (y-k)^2/b^2 = 1")

x_0 = float(input("Enter the X-coordinate of Center of Ellipse:"))
y_0 = float(input("Enter the Y-coordinate of Center of Ellipse:"))

a = abs(float(input("Enter value of a:")))
b = abs(float(input("Enter value of b:")))

if a!=b:
    t = np.linspace(0, 2*np.pi, 1000)
    x = x_0 + a*np.cos(t)
    y = y_0 + b*np.sin(t)
    
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_aspect=("equal")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_title("Ellipse")
    ax.set_xlim(min(x)-5, max(x)+5)
    ax.set_ylim(min(y)-5, max(y)+5)
    ax.scatter([x_0], [y_0], color='C3', zorder=3)
    ax.text(x_0, y_0, f'C ({x_0:.2f}, {y_0:.2f})', ha='left', va='bottom', fontsize=7)
    plt.savefig("figs/ellipse.png", dpi=300)
    plt.show()

else:
    print("Please Provide different Value of a and b")
