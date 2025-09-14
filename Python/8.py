import numpy as np

outer = np.ones([5,5])

zeros = np.zeros([3,3])
zeros[1,1] = 9
outer[1:4, 1:4]=zeros

print(outer)
