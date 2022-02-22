# Day 22/30 days with Python

# TUPLE
tup1 = tuple()  # constructor
tup2 = ( )  # tuple literal


explicit_tuple = (1, 2, 3, 'a', 'b')
implicit_tuple = 1, 2, 3, 'a', 'b'


# COUNT METHOD
tup = (1, 1, 1, 'a', 'a', 'a')
# print(tup.count(1))
# print(tup.count('a'))
# print(tup.count('c'))
# print(tup.count('d'))

# INDEX METHOD
# print(tup.index(1))
# print(tup.index('a'))

# INDEX AND SLICING
print(tup[1])
print(tup[3])
print(tup[5])



# SET
lst = [1, 1, 1, "a", "a", "b"]    # this is a list
tup = (1, 1, 1, "a", "a", "b")    # this is a tuple
nset = {1, 'a', "b"}              # this is a set (nset short for normal set)

nset1 = set()  # Constructor

# ADD METHOD
nset1.add(5)
nset1.add(7)
nset1.add('a')
nset1.add((1, 1, 'a'))

# print(nset1)

# nset1.add([1, 2, 3])

nset2 = {2, 3, 'a', 1, 'a'}
# print(nset2)

# REMOVE METHOD
nset2.remove(3)
# print(nset2)

# Removing a value that doesn't exist
# nset2.remove(5)

# DISCARD METHOD
nset2.discard(2)
print(nset2)








