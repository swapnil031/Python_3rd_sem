dict1 ={'ten':10,'twenty':20,'thirty':30}
dict2={'thirty':30,'forty':40,'fifty':50}
dict3=dict(dict1 | dict2)
print(dict3.items())
print(dict3.values())
print(dict3.keys())