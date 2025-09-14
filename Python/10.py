import numpy as np


a = np.ones((1,3))
b = np.array([1,2,3])

c = 4*a-b

c_t = c.reshape((3,1))

det = np.linalg.det(np.matmul(c,c_t))

print("|4a-b|=", int(det)+1)
print("Where a="+ str(a),"And b="+ str(b))
