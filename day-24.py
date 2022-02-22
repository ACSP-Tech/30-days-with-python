# Day 24/30 days with Python

# Functions

def intro():
    print("Hello World, Welcome to Python Programming")


# intro()
# intro()
# intro()
# intro()

# Return Statement
def add_func():
    return 5 * 2


new_add = add_func()
# print(new_add)
# print(intro())


# Function Scope
x = 5


def change_x(x):
    x = 10
    return x


# print(x)
# print(change_x(15))

lst = [1, 2, 3, 4]

def mutate_lst(lst):
    lst += ['a', 'b', 'c']
    print(lst)


mutate_lst(lst)

# Multiple Parameters
amount = int(input('Input the total amount: '))
percentage = int(input('Input the percentage: '))


def cal_perc(a, p):
    cal = a * p / 100
    return cal


print('percentage: ', cal_perc(amount, percentage))













