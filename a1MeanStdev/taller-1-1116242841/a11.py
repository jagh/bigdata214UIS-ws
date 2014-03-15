import numpy as np
import ct
import time
import glob

tstart = time.time()
threads=[]
r=[]

for fname in glob.glob("data*"):
   t=ct.CountThread(fname)
   t.start()
   threads.append(t)

for t in threads:
   t.join()
   r.append(t.q.get())	

r = np.array(r)
rsum = r.sum(axis=0)

#INSERTA TU CODIGO AQUi
sumx = rsum[0]
sumx2 = rsum[1] 
m = rsum[2]
suma = np.array([sumx,sumx2,m])

mean = sumx/m
stdv = np.sqrt((sumx2/m)-((sumx/m)*(sumx/m)))

print r
print "suma", suma

###
  # a11-Calcula mean/stdev
  # autor: john anderson garcia henao
  # 1116242841
#------------------------------
 
tend = time.time()
print "time = ",(tend-tstart)
print "mean = "+str(mean)
print "stdv = "+str(stdv)
print "m    = "+str(m)