n = 11
for i in range(n):
    for j in range(n-1):
        print(" ", end="")
    n -= 1
    for k in range(i):
        print("*", end=" ")
    print()