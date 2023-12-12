tuple1=(11,[22,33],44,55)
list1=list(tuple1)
print(list1)
if(22 in list1[1]):
    list1[1][0]=222
    #print('true')
tuple1=tuple(list1)
print(tuple1)