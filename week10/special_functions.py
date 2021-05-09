import numpy as np 
import matplotlib.pyplot as plt 

x=np.arange(0,3*np.pi,0.1)

y=np.sin(x)

#plotting the graph
plt.plot(x,y)

#making graphics appear
plt.show()