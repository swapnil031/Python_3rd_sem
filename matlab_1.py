import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,30,35,40,45,50])
y=np.array([1000,2000,3000,4000,5000,6000])
plt.plot(x,y,marker='o')
#plt.plot(x,y,'o:b')
plt.xlabel('Age')
plt.ylabel('Salary(RS)')
plt.title('Salary V/S Age')
#plt.grid(axis='x')
#plt.grid(axis='y')
plt.grid()
plt.show()