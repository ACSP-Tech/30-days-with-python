# Day 18/30 days with Python

# pop( ) method
print('\n\npop()...')

my_list = [1, 2, 3, "Hello", "World"]
print(my_list)

last_item = my_list.pop()
print('Last Item: ', last_item)
print(my_list)

my_list = [1, 2, 3, "Hello", "World"]
print(my_list.pop(2))



# index() method
print('\n\nindex()...')

print(my_list.index("Hello"))



# insert() method
print('\n\ninsert()...')
print(my_list)
my_list.insert(0, 50)
print(my_list)


# clear() method
print('\n\nclear()...')
my_list.clear()
print(my_list)

# count() method
print('\n\ncount()...')
my_list = [1, 2, 3, "Hello", "World", 1, 1]

print(my_list.count('HELLO'))


# reverse() method
print('\n\nreverse()...')

my_list = [1, 2, 3, "Hello", "World"]
print(my_list)

my_list.reverse()
print(my_list)


# sort() method
print('\n\nsort()...')

num_lst = [1, 0.5, 3.6, 17, 121, 12.1]
print(num_lst)

num_lst.sort()
print(num_lst)



