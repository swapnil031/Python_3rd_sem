friends=["soumik","srijan","uddalak","soutik","samiran"]
lucky_numbers=[1,2,3,4,5]
friends.append("hello")
print(friends)
friends.insert(1,"soudeep")
print(friends)
friends.extend(lucky_numbers)
print (friends[1:4])#print upto index 3
print(friends)
friends.remove("hello")
print(friends)
friends.pop()
print(friends)
print(friends.index("soumik"))