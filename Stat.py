from Processing import X, M, N
import numpy as np
import math


means = np.zeros(M)
median = np.median(X, axis=0)
sd = np.zeros(M)
maxes = np.zeros(M)
mins = np.zeros(M)
var = np.var(X,axis=0)
sim1 = np.zeros(M)

for i in range(M):
    means[i] = X[:,i].mean()
    maxes[i] = X[:,i].max()
    mins[i] = X[:,i].min()
    
myvar=np.zeros(M)
for j in range (M):
    for i in range(N):
        myvar[j] += ((X[i,j]-means[j]) ** 2)/(N-1)
        
for i in range(M):
    sd[i] = math.sqrt(myvar[i])
        
cov = np.zeros((M,M))
for i in range (M):
    for j in range(M):
        for k in range(N):
            cov[i,j] += ((X[k,i]-means[i]) * (X[k,j] - means[j]))/(N-1)
            
corr = np.zeros((M,M))

for i in range (M):
    for j in range(M):
        corr[i,j] = (cov[i,j]) / (sd[i] * sd[j])
