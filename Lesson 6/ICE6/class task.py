from sklearn.datasets import load_digits
from	sklearn	import svm

digits = load_digits()
X = digits.data
y = digits.target

estimator	= svm.SVC(gamma=0.001)
estimator.fit(X, y)
estimator.predict(x)





