from collections import defaultdict
"""
When the list class is passed as the default_factory argument, then a defaultdict is created with the values that are list.

"""
# Defining a dict
d = defaultdict(list)

for item in range(5):
    d[item].append(item+1)
print('Example1')
print("Dictionary with values as list:")
print(d)

"""
When the int class is passed as the default_factory argument, then a defaultdict is created with default value as zero.

"""

# Defining the dict
res2 = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count
for i in L:
    # The default value is 0
    # so there is no need to
    # enter the key first
    res2[i] += 1
print('Example2')
print(res2)

"""
It is a function returning the default value for the dictionary defined. If this argument is absent then the dictionary 
raises a KeyError.
"""
# Defining the dict and passing
# lambda as default_factory argument
res3 = defaultdict(lambda: "Not Present")
res3["a"] = 1
res3["b"] = 2
print('Example3')
print(res3["a"])
print(res3["b"])
print(res3["c"])
