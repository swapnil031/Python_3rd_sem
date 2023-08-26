num=input("enter a string")
i=0
while(i<len(num)-1):
    if(num[i] is num[i+1]):
        num[i+2]=num[i]
        num[i+3]=num[i+1]
    i=i+1