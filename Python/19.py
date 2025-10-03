import numpy as np
import matplotlib.pyplot as plt

X = ["Cola", "Pepsi", "ThumbsUp", "Water", "Real"]
Y = [100, 40, 30, 9, 21]
explodes=[0,0,0,0.4,0]

plt.pie(Y, labels=X, explode=explodes )
plt.show()

