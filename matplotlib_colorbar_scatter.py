import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([100,200,300,400,500])
colors = np.array([10, 20, 30, 40,50]) #default colour scale in matplotlib
plt.scatter(x,y,c=colors,cmap='viridis')

plt.grid()
plt.colorbar()
plt.show()