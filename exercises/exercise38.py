#EXERCISE 38 Doing things to list

ten_things = "Apple Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Lets fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

print("there we go:",stuff)
print("lets do some thing with stuff")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))