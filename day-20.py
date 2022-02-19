# Day 20/30 days with Python

# While Loop
print('\n\nWhile Loop...')

# counter = 1
#
# while counter <= 10:
#     print(counter)
#     counter += 1


# Using while loop with a collection
# beverages = ['water', 'juice', 'soda', 'tea', 'coffee']
#
# index = 0
# while index < len(beverages):
#     print(beverages[index])
#     index += 1


# Running conditional state and break
# beverages = ['water', 'juice', 'soda', 'tea', 'coffee']
#
# index = 0
# while index < len(beverages):
#     print(beverages[index])
#     index += 1
#     if beverages[index] == "soda":
#         print("We found soda!")
#         break


# Random Number
import random

num = random.randint(1, 5)
guess = int(input("Guess a random number from 1 to 5: "))

while guess != num:
    guess = int(input("Wrong guess. Try again (1 to 5): "))


print('Yes! You guessed correctly.')












