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

# #testng speed and conviency of umpy vs lists
# SIZE=1000

# L1=range(SIZE)
# L2=range(SIZE)

# #calculating sum in lists
# A1=np.arange(SIZE)
# A2=np.arange(SIZE)

# start = time.time()

# result= [(x,y) for x,y in zip(L1,L2)]

# print((time.time()-start)*1000)

# #for numpy 
# start=time.time()
# result=A1+A2
# print((time.time()-start)*1000) 