import numpy as np 
import matplotlib.pyplot as plt 
'''
sin,tan,cos
'''
x=np.arange(0,3*np.pi,0.1)

y=np.tan(x)

#plotting the graph
plt.plot(x,y)

#making graphics appear
plt.show()