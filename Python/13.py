import numpy as np


a = np.random.randint(1,10, size=(2,2))

print("A =", a)

b = np.linalg.matrix_power(a,2)
print("A^2 = B =", b)


if np.linalg.det(a)==0:
    print("A is not invertible as |A|=0")

else:
    c = np.linalg.inv(a)
    print("A^-1 = C =", c)
    print("AC=", np.matmul(a,c))



print("")
d = np.array([[1,2,3]])
e = np.random.randint(1,5, size =(1,3))

print("d*e=", d,"^T",e,"=",np.vdot(d,e))
print(" ")

for i in range(0,2):
    f = np.random.randint(1,3,size=(2,2), dtype='int16')
    f[1,1] = i
    print("Rank of", f,"=", np.linalg.matrix_rank(f))
    i +=1


print("")
g = np.random.randint(1,8, size=(3,3))
h = np.array([4,3,2])
h = np.vstack((h,h+1,h+2))
j =np.matmul(g,h)
j = j.astype('int32')
print(j)
