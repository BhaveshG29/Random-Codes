#CODE BY BHAVESH G


import numpy as np
import matplotlib.pyplot as plt

print("Consider the equation of Parabola as: \t y^2 = 4ax\n ")
print("Consider the equation of Circle as: \t (x-h)^2 + (y-k)^2 = r^2\n")
print("Considering the equation of Line as: \t y = mx +c\n")

a = float(input("Enter value of a:"))
h= float(input("Enter value of h:"))
k= float(input("Enter value of k:"))
r_2 = abs(float(input("Enter value of r^2:")))

r = np.sqrt(r_2)

#Mathematical conditions for parabola
t1 = np.linspace(0, 5, 100)
x_p = a*t1*t1
y_p1 = 2*a*t1
y_p2= -2*a*t1
F_x = a

#Mathematical conditions for Circle
t2 = np.linspace(0, 2*np.pi, 1000)
x_c = h + r*np.cos(t2)
y_c = k + r*np.sin(t2)

#Mathematical conditions for Line
m1 = float((k*(h-a) + r*np.sqrt((h-a)*(h-a) + k*k - r*r))/((h-a)*(h-a) - r*r))
m2 = float((k*(h-a) - r*np.sqrt((h-a)*(h-a) + k*k - r*r))/((h-a)*(h-a) - r*r))
c1 = -m1*a
c2 = -m2*a
x_l = np.linspace(-10, 100, 100)
y_l1 = m1*x_l + c1
y_l2 = m2*x_l + c2


fig, ax = plt.subplots()

#Labelling
ax.set_title("Solution Image")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

#Plotting Conics and Lines
ax.plot(x_p, y_p1, c="r", label="Parabola")
ax.plot(x_p, y_p2, c="r")
ax.plot(x_c, y_c, c="g", label="Circle")
ax.plot(x_l, y_l1, c="#000", ls="--", label="Line-1")
ax.plot(x_l, y_l2, c="#964B00", ls="--", label="Line-2")

#Plotting and Labelling Focus
ax.scatter(F_x,0, c="b", zorder=5, s=20, edgecolor="k", label="Focus")
ax.text(F_x-0.1, -0.6, "F", fontsize=10, fontweight="bold")

#Anonymous Atributes
ax.legend(loc="best")
ax.set_aspect("equal")
ax.grid(True)

#Adjusting Axises
ax.set_xlim(-2,h+r+5)
ax.set_ylim(-5, k+r+5)

#Saving Figure
plt.savefig("figure.png", dpi=400)

#Printing Line Equations
print("\n\nThe Equations of line are:\n")
print("y="+ str(m1) + "x +("+ str(c1)+ ")\n")
print("y="+ str(m2) +"x +"+ str(c2))
