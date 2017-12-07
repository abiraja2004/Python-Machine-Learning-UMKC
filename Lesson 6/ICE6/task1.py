from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB

#Loading the dataset
irisdataset=datasets.load_iris()

#getting the data and response of the dataset
x=irisdataset.data
y=irisdataset.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#split the data for training and testing
model = GaussianNB()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print(metrics.accuracy_score(y_test,y_pred))
