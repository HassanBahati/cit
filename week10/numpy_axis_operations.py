import numpy as np 
'''
rows-axis1 
cols-axis0
'''
a=np.array([(1,2,3),(3,4,5)])

#find sum of axis0
#1+3,2+4,3+5
print(a.sum(axis=0))

#sum of axis1
#1+2+3, 3+4+5
print(a.sum(axis=1))