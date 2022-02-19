# Day 19/30 days with Python

# Nested Lists
print('\n\nNested Lists...')

nested_list = [[2, 4, 12], ["A", "B", "C"], [6.5, 4.2, 10.0]]
print(nested_list[0])
print(nested_list[1])
print(nested_list[2])
print(len(nested_list))



# Getting Inner Elements
print('\n\nInner Elements...')
print(nested_list[0][0])
print(nested_list[1][1])
print(nested_list[2][2])



# Change Some Values
print('\n\nChange Values...')

nested_list2 = nested_list[:]
print(nested_list2)

nested_list3 = nested_list.copy()
print(nested_list3)

nested_list4 = nested_list
print('Nested List 4: ', nested_list4)

print('\n\nUpdated Values...')
nested_list[0][0] = 20
nested_list2[1][1] = "D"
nested_list3[2][2] = 40.0

print(nested_list)
print(nested_list2)
print(nested_list2)









