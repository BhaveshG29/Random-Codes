import numpy as np

a = np.zeros((6,5))

i = -3
j = -3
val = 1
for i in range(-1,5):
    i+=1
    for j in range(0,5):
        a[i,j]= val
        j+=1
        val +=1

print(a)
