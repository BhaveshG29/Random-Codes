#CODE BY BHAVESH G

import numpy as np
import matplotlib.pyplot as plt


print("Consider Polar Coordinate of Epispiral as:\n")
print("1)r=asec(n(θ)) \n2)r=a|sec(nθ)|")

Type= int(input("Enter 1 or 2 for the type of Epispiral: "))
a = float(input("Enter Value of a: "))
n = int(input("Enter Value of n: "))

t = np.linspace(0, 2*np.pi, 999999)

if Type==1:
    r = a/np.cos(n*t)
    x = r*np.cos(t)
    y = r*np.sin(t)

    fig, ax = plt.subplots()

    ax.set_title("Epispiral")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")

    ax.plot(x, y, c="r", label=f"r={a}sec({n}θ)")

    ax.set_xlim(-4*a, 4*a)
    ax.set_ylim(-4*a, 4*a)

    ax.grid(True)
    ax.set_aspect("equal")
    ax.legend()

    plt.savefig("figs/Epispiral1.png")
    plt.show()

elif Type==2:
    r = a/abs(np.cos(n*t))
    x = r*np.cos(t)
    y = r*np.sin(t)

    fig, ax = plt.subplots()

    ax.set_title("Epispiral")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")

    ax.plot(x, y, c="r", label=f"r={a}|sec({n}θ)|")

    ax.set_xlim(-4*a, 4*a)
    ax.set_ylim(-4*a, 4*a)

    ax.grid(True)
    ax.set_aspect("equal")
    ax.legend()

    plt.savefig("figs/Epispiral2.png")
    plt.show()

else:
    print("Please enter correct 1 or 2 for Type classification.")



