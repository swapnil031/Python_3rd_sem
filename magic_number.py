num=int(input("enter any number"))
magic=0
a=0
while(a>9 or num!=0):
    if(num==0):
        num=a
        a=0
    m=num%10
    a=a+m
    num=num//10
if(a is 1):
        print('magic no')
else:
     print('not')