import numpy as np
import math

a = np.genfromtxt('Sum.txt', delimiter = ',')
a = a.astype('int16')

a_t = a.reshape((3,1))

det = np.matmul(a,a_t)
print(math.sqrt(det[0]))
