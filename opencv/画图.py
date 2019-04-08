import numpy as np
import matplotlib as plt
import mat

T = np.linspace(0,1000)
X = np.sin(T)
Y = np.cos(T) + np.power(X,2/3)
plt.scatter(X,Y,C=Y)
plt.scatter(-X,Y,c=Y)
plt.axis([-2,2,-2,2])
plt.show()
