#MAP
def cube(x):
    return x*x*x
l=[]
newl1=[]
l=[int(item) for item in input('enter the list of numbers ').split(' ')]
newl1=list(map(cube,l)) #using map function
print(l)
print(newl1)

#FILTER

def greaterthan4(a):
    return a>4
newl2=list(filter(greaterthan4,l))
print(newl2)
    
#REDUCE
from functools import reduce # we need to import reduce to perform the reduce function
sum=reduce(lambda a,b:(a+b),l)
print(sum)