#num=int(input("enter the length of numbers"))
num=7
#k=num
for i in range(1,num+1):
    for k in range(0,num-i):#for k in range (1,num-i+1)
        print(" ",end="")
    #k=k-1
    for j in range(1,i+1):
        print(j,end=" ")
    print("\r")