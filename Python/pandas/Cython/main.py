import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cords = pd.read_csv("cords.csv")

X = np.array(cords["x"])
Y = np.array(cords["y"])

m = Y[0]/X[0]

print("Slope of Line =", m )

plt.plot(X, Y, c="r", ls="--", label="Line: y = mx")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)
plt.legend(loc="best")
plt.savefig("line.png", dpi=300)
plt.show()
