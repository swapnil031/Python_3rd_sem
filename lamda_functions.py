def func1(fx,data):
    return 4+fx(data)
square=lambda x:x*x
cube=lambda x:x*x*x
avg=lambda a,b:(a+b)/2
print(cube(2))
print(square(2))
print(avg(2,3))
print(func1(cube,5)) #print(func1(lambda x:x*x*x,5))