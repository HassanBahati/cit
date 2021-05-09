import numpy as np 
import sys
import time
'''
occupies lless spcae than lists in memory
faster than lists and more convient
'''

#prining a list- single dimensional array 
a=np.array([1,2,3]) 
print(a)

#2-dimensional array
a=np.array([(1,2,3),(4,5,6)])
print(a)

#getting spcae occupied by s
S = range(1000)
print(sys.getsizeof(5)*len(S))

#spce occupied by same but in numpy
D=np.arange(1000)
print(D.size*D.itemsize)

