# Day 23/30 days with Python

dct = dict()   # Constructor
dct = { }  # Dict Literal

# Keys: names or identifiers
# Values: data assigned to keys

beverages = {}
print(beverages)

# Setter
beverages["water"] = 1.25
beverages["soda"] = 1.25
beverages["tea"] = 1.50
beverages["juice"] = 1.75
beverages["coffee"] = 1.00

# print(beverages)

# Getter
# print(beverages['water'])
# print(beverages.get('tea'))

# Forloop print values
for drink in beverages:
    print(beverages[drink])

# Forloop print keys and values
for drink in beverages:
    print(drink, beverages[drink])









