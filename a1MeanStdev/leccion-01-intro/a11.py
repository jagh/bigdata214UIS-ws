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

# --- INSERTA TU CODIGO AQUÍ ----
sumx = ???
sumx2 = ???
m = ???

mean = ??
stdv  = ??
# --------------------------------
   
tend = time.time()
print "time = ",(tend-tstart)
print "mean = "+str(mean)
print "stdv = "+str(stdv)
print "m    = "+str(m)
