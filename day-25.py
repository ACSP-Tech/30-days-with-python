# Day 25/30 days with Python

# Classes and Objects

# class ThisIsAClass:  # Defining Class
# def this_is_a_function:  # Defining Function
# this_is_a_variable =  # Defining Variable

# Defining Class

# class Person:
#     def __init__(self):
#         self.name = 'John'

# our_set = list()
#
# the_person = Person()
# print(type(the_person))
#
# print(the_person.name)
#
#
# the_person.name = "Phil"
# print(the_person.name)


# Passing parameter to class
# class Person:
#     def __init__(self, name=None, age=None, married=False):
#         self.name = name
#         self.age = age
#         self.married = married
#
#
# john = Person("John", 25, True)
# mary = Person("mary")
# phil = Person("Phil")
# no_name = Person()
#
# print(john.name, john.age, john.married)
# print(mary.name)
# print(phil.name)
# print(no_name.name)


# Class Method
class Person:
    def __init__(self, name=None, age=None, married=False):
        self.name = name
        self.age = age
        self.married = married

    def hello(self):
        print("Hello!, It is nice to meet you.")

    def display(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Married: ', self.married)


john = Person("John", 25, True)
# print(john.name, john.age, john.married)

mary = Person("mary", 25)

# Reference method
# print(john.hello())

print(john.display())
print(mary.display())





















