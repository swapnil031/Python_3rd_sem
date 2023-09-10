tup=(13,2,3,"hello",12,13)
print(tup)
#print(len(tup))
if 12 in tup:
    print('yes')
else:
    print('no')
temp=list(tup) #conversion of tuple to list to perform list operations
temp.append(14)
tup=tuple(temp) #conversion of list to tuple
print(tup)
tup2=(22,23,"arko",'swapnil')
#we can add tuple
print(tup+tup2)
res=tup.index(13,3,len(tup))
print(res)