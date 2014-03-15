import numpy as np
import threading
import multiprocessing

class CountThread(multiprocessing.Process):
   def __init__ (self,filename):
      multiprocessing.Process.__init__(self)
      self.q = multiprocessing.Queue()
      self.filename = filename
      self.sumall=0
      self.sumsq=0
      self.nbelems=0
       
   def run(self):
      print "loading file "+self.filename
      a=np.loadtxt(self.filename)
      self.sumall = sum(a)
      self.sumsq  = sum(a**2)
      self.nbelems = a.shape[0]
      self.q.put(np.array([self.sumall, self.sumsq, self.nbelems]))

   