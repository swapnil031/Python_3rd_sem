import matplotlib.pyplot as plt
import numpy as np
a=np.array([1,2,3,4,5])
rollno=["Soumya","Swapnil","Soutik","Soudeep","Uddalak"]
myexplode = [0.2, 0, 0, 0,0]
plt.pie(a,labels=rollno,explode=myexplode)

plt.show()