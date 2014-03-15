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

r=np.array(r)

print "columns are [sum xi, sum xi^2, n]"
print r
print "sum "
print r.sum(axis=0)
