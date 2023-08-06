# https://tt-n-walters.github.io/hanoi/


def move_and_print(origin, destination):
    print("Move disk from", origin, "to", destination)


def move_and_append(origin, destination):
    instructions.append([origin, destination])


def solve(number_of_disks, origin, destination, other):
    if number_of_disks == 0:
        pass
    else:
        solve(number_of_disks - 1, origin, other, destination)
        move_and_print(origin, destination)
        solve(number_of_disks - 1, other, destination, other)


instructions = []
solve(4, "A", "B", "C")
