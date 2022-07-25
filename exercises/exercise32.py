#EXERCISE 32 Loops and Lists

count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'bananas']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

for number in  count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of types {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range (0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")