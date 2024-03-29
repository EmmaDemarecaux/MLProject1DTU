from Processing import X, y, M, N, attributeNames
import numpy as np
from matplotlib.pyplot import figure, legend, subplot, plot, title, xlabel, ylabel, show, grid, boxplot
from scipy.linalg import svd
from sklearn import preprocessing


X1 = np.squeeze(np.asarray(X))

figure(figsize=(14,6))
for i in range(6):
    subplot(1,6,i+1)
    boxplot(X1[:,i], sym='k.')
    title(attributeNames[i])
show()

# Subtract mean value from datya
Y = X - np.ones((N,1))*X.mean(0)

Y1 = np.squeeze(np.asarray(Y))
boxplot(Y1)

Xs = preprocessing.scale(X)
boxplot(Xs)

# PCA by computing SVD of Y
U,S,V = svd(Y,full_matrices=False)
V = V.T

# Project the centered data onto principal component space
Z = Y * V
Z1 = np.squeeze(np.asarray(Z))

# Compute variance explained by principal components
rho = (S*S) / (S*S).sum() 

# Plot variance explained
figure()
plot(range(1,len(rho)+1),rho,'o-')
title('Variance explained by principal components');
xlabel('Principal component');
ylabel('Variance explained');
grid()
show()

figure()
plot(X, y, 'o')
title('Wage vs Attributres')
xlabel('Attributes')
ylabel('Wage')
legend(attributeNames, loc=4)
show()

figure()
plot(Y, y, 'o')
title('Wage vs Attributres (mean subtracted)')
xlabel('Attributes')
ylabel('Wage')
legend(attributeNames, loc=4)
show()

figure()
plot(Xs, y, 'o')
title('Wage vs Attributres (mean scaled)')
xlabel('Attributes')
ylabel('Wage')
legend(attributeNames, loc=4)
show()

# Plot PCA of the data
figure()
plot(Z[:,0:M], y, 'o')
title('Wages : PCA')
xlabel('PCA')
ylabel('Wages')
legend(['PC' + str(i+1) for i in range (M)],loc=4)
show()

figure()
plot(Z[:,0:2], y, 'o')
title('Wages : PCA')
xlabel('PC1 and PC2')
ylabel('Wages')
legend(['PC1','PC2'],loc=4)
show()

Y2 = np.mat(np.empty((N,2)))
Y2[:,0] = Y[:,1]
Y2[:,1] = Y[:,0]
f = figure()
plot(Y2[:,0], y, 'o')
plot(Y2[:,1], y, 'o')
title('Projection onto iq and hours')
xlabel('')
ylabel('Wages')
legend(['iq','hours'],loc=4)
show()

i=0
Vmain=V[:,0:3]
f = figure()
title('Influence of each attribute on the variance')
plot(Vmain)
legend(['PC{0}'.format(i+1),'PC{0}'.format(i+2),'PC{0}'.format(i+3)])
xlabel(attributeNames)
show()

Us,Ss,Vs = svd(Xs,full_matrices=False)
Vs = Vs.T

# Project the centered data onto principal component space
Zs = Xs.dot(Vs)
Z1 = np.squeeze(np.asarray(Z))

# Compute variance explained by principal components
rhos = (Ss*Ss) / (Ss*Ss).sum() 

# Plot variance explained
figure()
plot(range(1,len(rhos)+1),rhos,'o-')
title('Variance explained by principal components');
xlabel('Principal component');
ylabel('Variance explained');
grid()
show()

# Plot PCA of the data
figure()
plot(Zs[:,0:M], y, 'o')
title('Wages : PCA')
xlabel('PCA')
ylabel('Wages')
legend(['PC' + str(i+1) for i in range (M)],loc=4)
show()

figure()
plot(Zs[:,0:2], y, 'o')
title('Wages : PCA')
xlabel('PC1 and PC2')
ylabel('Wages')
legend(['PC1','PC2'],loc=4)
show()

i=0
Vsmain=Vs[:,0:4]
f = figure()
title('Influence of each attribute on the variance')
plot(Vsmain)
legend(['PC{0}'.format(i+1),'PC{0}'.format(i+2),'PC{0}'.format(i+3),'PC{0}'.format(i+4)])
xlabel(attributeNames)
show()
