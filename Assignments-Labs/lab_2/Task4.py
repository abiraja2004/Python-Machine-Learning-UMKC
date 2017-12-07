import numpy as np

Z = np.random.rand(15)
z1=Z.argmax()

print("the maximum number in the set it ",Z[z1]," and its place is ",z1)
Z[z1] = 100
print("set after placing the maximum value with 100",Z)
