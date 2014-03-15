import numpy as np
import sys
import glob

nargs = len(sys.argv)

if nargs!=3:
   print "incorrect number of arguments"
   print "   "+sys.argv[0]+" nbfiles nbelemnts-per-file"
   exit(-1)

nbfiles=int(sys.argv[1])
nbelems=int(sys.argv[2])

files = glob.glob("data.*")

if len(files)>0:
   print "data files exist. erase them before for safety"
   print "aborting ..."
   exit(-1)

for i in range(0,nbfiles):
   d=np.random.rand(nbelems)*10
   np.savetxt("data."+str(i+1),d, fmt="%2.4f")
   print "created file "+str(i+1)
