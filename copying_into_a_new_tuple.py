tup1=(11,22,33,44,55,66)
temp=list(tup1)
temp2=[]
if(44 in temp):
    temp2.append(44)
if(55 in temp):
    temp2.append(55)
tup1=tuple(temp)
print(tup1)
tup2=tuple(temp2)
print(tup2)
