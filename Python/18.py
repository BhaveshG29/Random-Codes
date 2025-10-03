import numpy as np
import matplotlib.pyplot as plt

X = [0]
Y = [0]

for i in range(-50,51):
    X.append(i)
    Y.append(5*i)

plt.plot(X,Y, c="red")
plt.scatter(0,0, c="blue", s=50)
plt.show()

