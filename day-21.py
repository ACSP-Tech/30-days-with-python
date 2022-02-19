# Day 21/30 days with Python

# For Loop
# print('\n\nFor Loop...')
#
# for i in range(0, 10, 2):
#     print(i)
#
# print('\n\nRange and slice...')
#
# for i in range(10)[:5]:
#     print(i)


print('\n\nForloop on collections...')
# Running Forloop in collections
beverages = ['water', 'juice', 'soda', 'tea', 'coffee']

for i in range(len(beverages)):
    print(beverages[i])
    if beverages[i] == 'juice':
        print("We found juice!")
        break





