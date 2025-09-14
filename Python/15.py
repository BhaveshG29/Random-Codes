import numpy as np

a = np.array([7,-6,1])
b = np.array([1,-2,1])

c =abs(np.cross(a.T,b))

print(c)
