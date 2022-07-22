# Exercise 30 Else and if

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take cars.")
elif cars < people:
    print("We should not take cars.")
else:
    print("we cant decide.")

if trucks > cars:
    print("Too many trucks")
elif trucks < cars:
    print("take the trucks")
else: 
    print("we still cant decide.")

if people > trucks:
    print("Alright, lets just take the trucks.")
else:
    print("Fine, lets stay home.")