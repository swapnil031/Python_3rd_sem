num=[1,2,3,2,3,5]
num2=[]
z=0
for i in range(0,len(num)):
    j=i+1
    while(j<len(num)):
        if(num[i]==num[j]):
            num2.append(num[j])
            num.pop(j)
        j+=1
num.extend(num2)
print(num)