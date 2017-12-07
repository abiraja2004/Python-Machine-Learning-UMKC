from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn import svm, datasets
from sklearn.datasets import load_boston,load_digits

C = 1.0
#getting the data and response of the dataset
digits=load_digits()
x=digits.data
y=digits.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model = svm.SVC(kernel='linear')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Accuracy for SVC linear " + str(metrics.accuracy_score(y_test,y_pred)))
model = svm.SVC(kernel='rbf')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Accuracy for SVC with kernel rbf "+str(metrics.accuracy_score(y_test,y_pred)))
