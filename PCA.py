import matplotlib.pyplot as plt
import numpy as np


k = 2

X = np.array([
    [4, 2, 3],
    [6, 1, 3],
    [4, 2, 5],
    [7, 8, 3]])

print('shape of X =' , X.shape)
print('\n ----------------------------------------------------------------------\n')

print('Lets compute mean row vectors first\n')
meanrow = np.zeros((1,X.shape[1]))
for i in range(X.shape[1]):
     meanrow[0,i] = sum(X[:,i]/X.shape[0])
print(meanrow)
print('\n ----------------------------------------------------------------------\n')

print('lets compute mean row matrix')
meanrowmatrix = np.ones((X.shape[0],1)) * meanrow
print(meanrowmatrix)
print('\n ----------------------------------------------------------------------\n')

print('Substracting mean')
B = X - meanrowmatrix
print(B)
print('\n ----------------------------------------------------------------------\n')

print('compute covariance matrix')
covariance_matrix = B.T.dot(B) / X.shape[0]
print(covariance_matrix)
print('\n ----------------------------------------------------------------------\n')

print("compute k largest eigenvectors")
eigenValues, eigenVectors = np.linalg.eig(covariance_matrix)
idx = eigenValues.argsort()[::-1]
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:,idx]
print("eigenVectors")
print(eigenVectors)
print("eigenValues",eigenValues)
print("------------------------------------")
print(f'Check if Av1 = lambda1 v1:\nAv1 = {covariance_matrix.dot(eigenVectors[:, 0])}\nlambda1 v1 = {eigenValues[0]*eigenVectors[:, 0]}')
print("------------------------------------")
print(f'Check if Av2 = lambda2 v2:\nAv2 = {covariance_matrix.dot(eigenVectors[:, 1])}\nlambda2 v2 = {eigenValues[1]*eigenVectors[:, 1]}')
print('\n ----------------------------------------------------------------------\n')

print("compute W")
W=eigenVectors[:,0:k]
print(W)
print(W.shape)

print('\n ----------------------------------------------------------------------\n')

print("we will do projection now")
for i in range(X.shape[0]):
    transformed = W.T.dot(X[i, :])
    plt.scatter(transformed[0],transformed[1])
    print("transformed= ", i, " ", transformed)
    print("------------------------------------")
print('\n ----------------------------------------------------------------------\n')


if k==2:
    plt.show()
    plt.savefig("PCA_tutorial.png")
    print("END")
