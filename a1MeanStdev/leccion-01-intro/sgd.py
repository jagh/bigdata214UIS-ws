import numpy as np
import matplotlib.pyplot as plt
from sgd import *
   
def create_random_dataset (n_points, n_dims=1, xmin=0, xmax=1, noise=0.01   ):
   theta = np.random.random(n_dims+1)*2-1
   X = np.hstack((np.ones((n_points,1)), np.random.random((n_points,n_dims))*xmax+xmin))
   y = X.dot(theta) + np.random.normal(0,(xmax-xmin)*noise,n_points)
   return X,y,theta

def plotline(X, theta, color="r"):
   i = np.argsort(X[:,1])
   plt.plot (X[i][:,1], X[i].dot(theta), color=color)

def error(theta,X,y):
   return np.sum(np.sqrt((X.dot(theta)-y)**2))/X.shape[0]

# ajusta con gradiente descendente
def fit_gd(X,y, n_iters=20, alpha=0.1):
   theta,n = np.zeros(X.shape[1]), X.shape[0]
   errors = []
   theta_list = []; theta_list.append(theta)
   for j in np.arange(0,n_iters):
      theta = theta - alpha*X.T.dot(X.dot(theta)-y)/n
      theta_list.append(theta)
      errors.append(error(theta,X,y))
      
   theta_list = np.array(theta_list).reshape(n_iters+1,X.shape[1])

   return theta, stretch(errors, n), theta_list

# ajusta con gradiente descendente estocastico
def fit_sgd(X,y, n_iters=20, alpha=0.1):
   theta,n = np.zeros(X.shape[1]), X.shape[0]
   theta_list = []; theta_list.append(theta)
   errors = []
   for j in np.arange(0,n_iters):   
      for jj in np.arange(0, X.shape[0]):
         i = np.random.randint(X.shape[0])
         xi = np.array([X[i]])
         theta = theta - alpha*xi.T.dot(xi.dot(theta)-y[i])/n
         theta_list.append(theta)
         errors.append(error(theta,X,y))

   theta_list = np.array(theta_list).reshape(n_iters*n+1,X.shape[1])

   return theta, errors, theta_list

# 'stretches' an array. i.e [1,2,3], factor=3 --> [1,1,1,2,2,2,3,3,3]
def stretch(a, factor):
   l = len(a)
   s = np.zeros(l*factor)
   for i in np.arange(0,l):
      for j in np.arange(0,factor):
         s[i*l +j] = a[i]
   return s

