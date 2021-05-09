'''
sd- calculate the sum and check how much the numbers deviate from that mean
'''

import numpy as np 
a=np.array([(1,2,3),(3,4,5)])

#square root of the elements of the array
print(np.sqrt(a))

#standard deviation-how much each deviates from mean
print(np.std(a))