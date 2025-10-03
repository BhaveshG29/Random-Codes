#CODE BY BHAVESH G
import matplotlib.pyplot as plt
import math

Type = int(input("Enter 1 for y^2=4ax and 2 for x^2 = 4ay:"))
a = float(input("Enter the value of a:"))

if Type==1:
    X=[0]
    Y=[0]
    Y_minus = [0]
    for i in range(1,1234):
        X.append(i)
        Y.append(2*math.sqrt(abs(a))*math.sqrt(X[i-1]))
        Y_minus.append(-2*math.sqrt(abs(a))*math.sqrt(X[i-1]))
    plt.plot(X, Y, c="r", lw=3, label="y^2 = 4ax")    
    plt.plot(X,Y_minus, c="r", lw=3)

elif Type==2:
    X=[0]
    Y=[0]
    X_minus = [0]
    for i in range(1,1234):
        Y.append(i)
        X.append(2*math.sqrt(abs(a))*math.sqrt(Y[i-1]))
        X_minus.append(-2*math.sqrt(abs(a))*math.sqrt(Y[i-1]))
    plt.plot(X, Y, c="b", lw=3,  label="x^2 = 4ay")    
    plt.plot(X_minus,Y, c="b", lw=3)

else:
    print("Please Enter 1 or 2 in type")


plt.legend()
plt.title("Parabola")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig("figs/Parabola.png", dpi=300)
plt.show()
