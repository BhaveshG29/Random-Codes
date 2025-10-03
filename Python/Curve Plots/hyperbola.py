#CODE  BY BHAVESH G

#CODE BY BHAVESH G
import numpy as np
import matplotlib.pyplot as plt

print("Considering Equations of Hyperbola as:\n")
print("Equation of Hyperbola as (1) \t (x-h)^2/a^2 - (y-k)^2/b^2 = 1)\n")
print("Equation of Hyperbola as (2) \t -(x-h)^2/a^2 + (y-k)^2/b^2 = 1)\n")
print("Equation of Hyperbola as (3) \t (x-h)(y-k) = c^2)\n\n")

Type = int(input("Enter the number of hyperbola of you want:"))


h = float(input("Enter X-coordinate of center of Hyperbola:"))
k = float(input("Enter Y-coordinate of center of Hyperbola:"))


if Type==1:
    a = abs(float(input("Enter the value of a:")))
    b = abs(float(input("Enter the value of b:")))
    t = np.linspace(0,2*np.pi, 1000)
    x = h + a/np.cos(t)
    y = k + a*np.tan(t)

    fig, ax = plt.subplots()
    ax.set_title("Hyperbola")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.plot(x,y)
    ax.scatter(h,k, color="red")
    ax.set_aspect("equal")
    ax.set_xlim(-h-a-20, h+a+20)
    ax.set_ylim(-k-b-15, k+b+15)
    plt.savefig("figs/hyperbola.png", dpi=299)
    plt.show()

elif Type==2:
    a = abs(float(input("Enter the value of a:")))
    b = abs(float(input("Enter the value of b:")))
    t = np.linspace(0,2*np.pi, 1000)
    y = k + a/np.cos(t)
    x = h + a*np.tan(t)

    fig, ax = plt.subplots()
    ax.set_title("Hyperbola")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.plot(x,y)
    ax.scatter(h,k, color="red")
    ax.set_aspect("equal")
    ax.set_xlim(-h-a-15, h+a+15)
    ax.set_ylim(-k-b-20, k+b+20)
    plt.savefig("figs/hyperbola.png", dpi=299)
    plt.show()

elif Type==3:
    c = abs(float(input("Enter the value of c:")))
    t = np.linspace(0, 2*np.pi, 1000)
    x = c*np.tan(t)
    y= c/np.tan(t)
    fig, ax = plt.subplots()
    ax.set_title("Hyperbola")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.plot(x,y)
    ax.scatter(h,k, color="red")
    ax.set_aspect("equal")
    ax.set_xlim(-h-c-20, h+c+20)
    ax.set_ylim(-k-c-20, k+c+20)
    plt.savefig("figs/hyperbola.png", dpi=299)
    plt.show()
    

else:
    print("Please Enter the correct index. for results")


