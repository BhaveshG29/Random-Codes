#CODE BY BHAVESH G

import matplotlib.pyplot as plt
import math

X_0 = float(input("Enter the X-coordinate of Center:"))
Y_0 = float(input("Enter the Y-coordinate of Center:"))
R = abs(float(input("Enter the radius of the Circle:")))

X = [X_0]
Y = [Y_0]

for i in range(1,700):
    X.append(X_0 + R*math.cos(i))
    Y.append(Y_0 + R*math.sin(i)) 

plt.plot(X,Y, c="r", lw=0.1)
plt.scatter(X_0, Y_0, c="b")
plt.title("Cirlce (x-a)^2 + (y-b)^2 = r^2")
plt.savefig("figs/circle", dpi=300)
plt.show()
