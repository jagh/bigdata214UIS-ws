import numpy as np
import matplotlib.pyplot as plt
from sgd import *

n_dims,n_iters, n_points, noise = 1, 100,100, 0.02

X,y, theta = create_random_dataset(n_dims=n_dims, n_points=n_points, noise=noise)

gd_theta, gd_error, gd_theta_list    = fit_gd(X,y, n_iters=n_iters, alpha=0.7)
sgd_theta, sgd_error, sgd_theta_list = fit_sgd(X,y, n_iters=n_iters, alpha=0.7)

# plot dataset in 1D case
if X.shape[1]==2:
   plt.scatter(X[:,1],y)
   for i in np.arange(0,len(gd_theta_list)/3):
     plotline(X,gd_theta_list[i*3], color="gray") 
   plotline(X, gd_theta, color="r")
   plt.scatter(X[:,1],y)
   plt.figure()
   
   
# plot evolution of errors
plt.plot(gd_error, color="r")
plt.plot(sgd_error, color="g")

   
# plot evolution of theta over iterations
plt.figure()

tmin = gd_theta_list.min()-0.2
tmax = gd_theta_list.max()+0.2
cg = 40
theta_r = np.random.random((cg**2,gd_theta_list.shape[1]))*(tmax-tmin)+tmin
t1,t2 = np.meshgrid(np.arange(tmin,tmax,(tmax-tmin)/cg), np.arange(tmin,tmax,(tmax-tmin)/cg))
theta_r[:,0]=t1.flatten()
theta_r[:,1]=t2.flatten()
terr = np.array([error (t,X,y) for t in theta_r])
plt.contourf(theta_r[:,0].reshape(cg,cg), theta_r[:,1].reshape(cg,cg), terr.reshape(cg,cg), cmap=plt.cm.gray_r)

plt.plot(gd_theta_list[:,0], gd_theta_list[:,1], color="r")
plt.scatter (gd_theta_list[-1,0], gd_theta_list[-1,1], color="r")
plt.plot(sgd_theta_list[:,0], sgd_theta_list[:,1], color="g")
plt.scatter (sgd_theta_list[-1,0], sgd_theta_list[-1,1], color="g")
plt.scatter (theta[0], theta[1])


plt.show()
