#EXERCISE 21 Function can Return Something

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print(" lets do some math with just functions!")

age = add(20, 20)
height = subtract(78, 4)
weight = multiply(50, 2)
iq = divide(200, 2)

print(f"Age: {age} Height: {height} Weight: {weight} IQ: {iq}")

print("here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("result", what)