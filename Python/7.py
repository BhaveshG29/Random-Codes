import math
import numpy as np

i=input("Enter a Number: ")
s = 0

while int(i)<40:
    print(i)
    i = pow(int(i), 2)
    s += i

print(s)
