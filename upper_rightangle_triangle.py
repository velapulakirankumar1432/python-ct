n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    for space in range(n - i):
        print(" ", end=" ")
    for star in range(i):
        print("*", end=" ")
    print()
