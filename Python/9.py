import numpy as np


a = np.array([[1,2],[12,13],[3,23]])
b = np.full([3,3], 2)
c = np.full([2,3], 2)

d = np.matmul(a,c)
e = np.matmul(d,b)

print(d)
print(e)

det = np.linalg.det(e)
print("|e|=", det)
