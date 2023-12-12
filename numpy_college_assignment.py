import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

#addition of diagonal elements
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
x=np.diag(a)
print(x)
i=0
y=0
while(i<np.size(x)):
    y=x[i]+y
    i+=1
print(y)


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.add(a,b)
print(y)


#adding coloumns to an array
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([3,3,3])
x=np.c_[a,b]
print(x)


#adding rows to an array
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([3,3,3])
x=np.r_[a,[b]]
print(x)


#calculating eigen values
import numpy as np
from numpy import linalg as lg
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
x=lg.eigvals(a)
print(x)


#calculating determinant of an array
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
x=np.linalg.det(a)
print(x)

#calculating inverse of an matrix
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
x=np.linalg.inv(a)
print(x)


#frequency of elements in an array
import numpy as np
a=np.array([1,1,2,3,4,5,5,6.7])
elements,frequency=np.unique(a,return_counts = True)
print("array is ",elements)
print("frequency is",frequency)

#finding covariance
import numpy as np
a=np.array([1,2,3])
b=np.array([3,4,5])
c=np.cov(a,b)
print(c)


#calculating inner,outer and cross product of matrices
import numpy as np
x = np.array([[2, 3, 4], [3, 2, 9]]) 
y = np.array([[1, 5, 0], [5, 10, 3]]) 
a=np.inner(x,y)
b=np.outer(x,y)
c=np.cross(x,y)
print(a)
print(b)
print(c)