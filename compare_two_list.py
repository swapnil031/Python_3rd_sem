list1=[1,2,3,4,5]
list2=[1,2,3,4,6]
n=len(list1)
i=0
index=0
while(i<n):
    if(list1[i]!=list2[i]):
        index=i
        break
    i+=1
print("the uncommon index is",index)