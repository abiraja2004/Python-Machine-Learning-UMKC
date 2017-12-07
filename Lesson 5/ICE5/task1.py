import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])


beta1 = np.divide(np.sum(np.multiply((x-np.mean(x)),(y-np.mean(y)))),np.sum(np.multiply((x-np.mean(x)),(x-np.mean(y)))))
beta0 = np.mean(y)-beta1*np.mean(x)

plt.scatter(x,y,color="yellow")
y=beta0+beta1*x
plt.plot(x,y,color="red")
plt.show()


