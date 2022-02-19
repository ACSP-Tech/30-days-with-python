# Day 17/30 days with Python

# append( ) method
# list1 = list()
# print(list1)
#
# list2 = []
# print(list2)
#
# print(len(list2))


# Placing Value is List Variable
grocery_list = []
grocery_list.append('Milk')
grocery_list.append('Egg')
grocery_list.append('Bread')
grocery_list.append('Rice')
print(grocery_list)
print(len(grocery_list))


# Indexing List
print('Index 0: ', grocery_list[0])
print('Index 1: ', grocery_list[1])
print('Index 2: ', grocery_list[2])
print('Index 3: ', grocery_list[3])


# Out or range index
# print('Index Outrange: ', grocery_list[5])

# Negative Indexing
print('THIS ARE NEGATIVE INDEX...')
print('Index -1: ', grocery_list[-1])
print('Index -2: ', grocery_list[-2])
print('Index -3: ', grocery_list[-3])
print('Index -4: ', grocery_list[-4])


# List is mutable
print('\n\nMUTABLE...')
grocery_list[0] = "Juice"
print(grocery_list)


# Slicing list
print('\n\nSlicing...')
your_list = grocery_list[:2]
your_list2 = grocery_list[2:]
print(your_list2)


# Out of range wont raise error
print('\n\nOUT OF RANGE...')
my_slice = grocery_list[15:15]
print(my_slice)








