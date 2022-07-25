#EXERCISE 33 While loops

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("NUmber now:", numbers)
    print(f"At the bottom i  is {i}")
print("the numbers:")
for num in numbers:
    print(num)