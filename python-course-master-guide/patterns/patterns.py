print("Square")
for row in range(7):
    for col in range(7):
        print("x", end=" ")
    print()  # Starting a new line


print("Growing triangle")
for row in range(7):
    for col in range(7):
        if col <= row:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()  # Starting a new line


print("Shrinking triangle")
# for row in range(6, -1, -1):
for row in range(7):
    for col in range(7):
        if col < 7 - row:
            print("x", end=" ")
        else:
            print("-", end=" ")
    print()  # Starting a new line


print("Hollow sqaure")
for row in range(7):
    for col in range(7):
        if row == 0 or row == 6 or col == 0 or col == 6:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()
