import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,1,2,3])
y=np.array([10,15,20,25])
plt.subplot(2,2,1)   # 2 rows 2 coloumns and 1st sub graph
plt.grid()
plt.title('First')
plt.plot(x,y)

x=np.array([0,1,2,3])
y=np.array([30,35,40,45])
plt.subplot(2,2,3)  
plt.grid()
plt.title("Third")
plt.plot(x,y)

x=np.array([0,1,2,3])
y=np.array([50,55,60,65])
plt.subplot(2,2,2)
plt.grid()
plt.title("Second")
plt.plot(x,y)

x=np.array([0,1,2,3])
y=np.array([70,35,40,45])
plt.subplot(2,2,4)
plt.grid()
plt.title("Fourth")
plt.plot(x,y)

plt.suptitle('Practice')
plt.show()
