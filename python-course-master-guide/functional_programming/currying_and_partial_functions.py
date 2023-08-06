# Higher-order functions are functions that accept other functions as an argument.

# First-class functions are when functions can be treated as variables.

# Currying is a functional programming technique to further simplify functions.

# Partial functions (partial application) are one way to implement Currying.


# Arity  = the number of arguments to a function
# str(10) has an arity of 1


def multiply(a):
    print("Received a:", a)
    def xyz(b):
        print("Received b:", b)
        return a * b
    return xyz

# first = multiply(10)
# answer = first(2)

# print(answer)


from functools import partial

def multiply(a, b):
    print("Received a:", a)
    print("Received b:", b)
    return a * b

# first = partial(multiply, 10)
# answer = first(2)

# print(answer)



x = int("1011", base=2)
# print(x)
# print(type(x))

_1011 = partial(int, "1011")

# print(_1011(base=2))
# print(_1011(base=3))
# print(_1011(base=4))
# print(_1011(base=5))
# print(_1011(base=6))


binary = partial(int, base=2)

# print(binary("10110011010101110101011"))
# print(binary("1001"))
# print(binary("11011"))

#  0123456789abcdef
hexadecimal = partial(int, base=16)
# print(hexadecimal("0x2A"))



import math
import random

def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

enemies = [[random.randint(-50, 50), random.randint(-50, 50)] for _ in range(20)]
player = [5, 5]

# def distance(a):
#     def distance(b):
#         x1, y1 = a
#         x2, y2 = b
#         return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     return distance

# distance_from_player = distance(player)


distance_from_player = partial(distance, player)
result = sorted(enemies, key=distance_from_player)
print(result)



# distances = {}
# smallest = 99999999
# for enemy in enemies:
#     number = distance(player, enemy)
#     distances[number] = enemy
#     if number < smallest:
#         smallest = number





# print(smallest)
# print(distances[smallest])