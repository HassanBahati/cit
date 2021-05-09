import numpy as np

#array with 2 rows
a=np.array([(1,2,3,4),(3,4,5,6),(7,8,9,10)])

#slicing from index 0 get its index 2
print(a[0,2])
  
#print 4 and 6
#check all rows and get the index 3 
#0: means check all rows including the 1st
print(a[0:2,3])

#including the last 
print(a[0:,3])

#print all the 5 values taht equally spaced btn 1 and 3
a=np.linspace(1,3,5)
print(a)

#10 values equally spaced between 1 and 3
a=np.linspace(1,3,10)
print(a)