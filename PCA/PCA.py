import numpy as np 
import math
from scipy import linalg
from sklearn import decomposition
from numpy import linalg as LA

def PCA_by_SVD(data):
    m, n = data.shape
    mn = np.mean(data, axis = 1)
    mean_data = []
    mean_data_son = []
    for i in range(m):
        for j in range(n):
            mean_data_son.append(mn[i])
        mean_data.append(mean_data_son)
        mean_data_son = []
    mean_data = (data - np.array(mean_data))
    u, s, v = linalg.svd(mean_data.T / math.sqrt(n - 1))
    print np.dot(v, mean_data)

def PCA_by_Eigenvector(data):
    m, n = data.shape
    mn = np.mean(data, axis = 1)
    mean_data = []
    mean_data_son = []
    for i in range(m):
        for j in range(n):
            mean_data_son.append(mn[i])
        mean_data.append(mean_data_son)
        mean_data_son = []
    mean_data = (data - np.array(mean_data))
    w, v = LA.eig(np.dot(mean_data, mean_data.T) / (n - 1))
    indices = sorted(range(len(w)), key = lambda k : w[k])
    PC = []
    for i in range(len(indices)):
        PC.append(v[indices[i]])
    PC = np.array(PC)
    print np.dot(PC.T, mean_data)

#Small Ball's Motion 
data = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])

#Get result from PCA method of sklearn
pca = decomposition.PCA()
data_trans = pca.fit_transform(data.T)
print data_trans

#Perform PCA Using SVD
PCA_by_SVD(data)

#Perform PCA Using Eigen decomposition
PCA_by_Eigenvector(data)