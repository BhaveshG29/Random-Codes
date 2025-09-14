import numpy as np

a = np.genfromtxt("sum.dat", delimiter=',')
a = a.astype('int16')

a_t = a.reshape((4,1))

b = np.random.randint(1,21, size=(4,4)) 

print(b, "\n")

if np.linalg.det(b)==0:
    print("|b|=0")

elif np.linalg.det(b)!=0:
    c = np.linalg.inv(b)
    print(np.linalg.det(b),"\n")
    print(c,"\n")
    print("AxC=",np.matmul(a,c),"Rank of C=",np.linalg.matrix_rank(c), "\n")



print(a_t, np.matmul(a,a_t), "\n")
