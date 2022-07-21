#EXERCISE 19 Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that enough for a party")
    print("get a blanket.")

print("we can just give the function numbers directly")
cheese_and_crackers(20, 30)
print("or, we can use the variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too:")
cheese_and_crackers(20+30, 42+39)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+20, amount_of_crackers+20)

