'''
reshape - change of cols and rows
==slicing
'''

import numpy as np 

a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
#reshape to 4 rows and 2 cols
a=a.reshape(4,2)

print(a)


