def search(a:int,list2):
    #print(n)
    for i in list2:
        #print(i)
        #print(type(i))
        #print(list2)
        if(i==a):
            return "found"
    return "not found"
#n=int(input("enter the size of the list"))
num=[]
num= [int(item) for item in input("enter number").split(',')] #taking input of list in python
print(num)
print(len(num))
print("enter the no you want to search:")
a=int(input())
print(search(a,num))
