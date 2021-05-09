import numpy as np 


a=np.array([(1,2,3),(3,4,5)])

b=np.array([(1,2,3),(3,4,5)])


#verticcal stacking 
print(np.vstack((a,b)))

#horizontal stacking
print(np.hstack((a,b)))