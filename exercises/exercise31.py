# Exercise 31 Making decisions

print(""" You entr adark room with two rooms.
Do you go through #1 or door #2?""")

door = input("> ")
if door == '1':
    print("There is a gaint bear eating a cheese cake.")
    print("what do you do?")
    print("take the cake.")
    print("scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("the bear eats your leg off. Good job!")
    else:
        print(f" well done {bear} is probably better.")
        print("bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at there.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespin.")
    print("Understanding revolvers yeling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello.")
        print("Good job!")
    
    else:
        print("the insanity rots your eyes into a pool of muck.")
        print("good job!")
else:
    print("die. good job!")
