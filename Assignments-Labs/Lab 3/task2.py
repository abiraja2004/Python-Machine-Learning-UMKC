import csv

import numpy as np
import matplotlib.pyplot as plt
import random

from sklearn.cluster import KMeans



CustomerID = []
Genre = []
Age = []
Annual_income= []
Spending_Score = []

def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    #plt.figure()
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()


def cluster_content(X, mu):
    cluster = {}
    for x in X:
        value = min([(i[0],np.linalg.norm(x - mu[i[0]]))for i in enumerate(mu)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster

def Apply_Kmeans(X, K, N):
    temp1 = np.random.randint(N, size = K)
    oldmu = np.array([X[i]for i in temp1])
    temp2 = np.random.randint(N, size=K)
    newmu = np.array([X[i] for i in temp2])
    cluster = cluster_content(X, oldmu)
    itr = 0
    plot_cluster(oldmu,cluster,itr)
    while not matched(newmu, oldmu):
        itr = itr + 1
        oldmu = newmu
        cluster = cluster_content(X,newmu)
        plot_cluster(newmu, cluster,itr)
        newmu = new_center(newmu, cluster)
    plot_cluster(newmu, cluster, itr)
    return

def new_center(mu, cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    #for k in keys:
    #    newmu.append(np.mean(cluster[k],axis = 0))
    return newmu

def matched(newmu, oldmu):
    return (set([tuple(a)for a in newmu]) == set([tuple(a)for a in oldmu]))

#downloaded data from https://www.google.com/finance/historical?cid=304466804484872&startdate=Jun+15%2C+2016&enddate=Jun+30%2C+2016&num=30&ei=WbVaWdHkN4fjjAG2l6OwCA
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            #print(', '.join(row))
            CustomerID.append(int(row[0]))
            Genre.append(str(row[1]))
            Age.append(int(row[2]))
            Annual_income.append(int(row[3]))
            Spending_Score.append(int(row[4]))
    return

get_data('Customers.csv')
'''
K = 5 # as defined in task 2
X = np.array([[CustomerID,Age,Annual_income,Spending_Score]])
X = np.reshape(X, (len(X.T), 4))
temp = Apply_Kmeans(X, K,200)
'''


K = 5 # as defined in task 2
X = np.array([[Spending_Score,Annual_income,Age,CustomerID]])
X = np.reshape(X, (len(X.T), 4))
temp = Apply_Kmeans(X, K,200)