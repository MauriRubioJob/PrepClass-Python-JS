from functools import reduce

# High order function
# A function that accepts another function, as an argument.

map
filter
reduce


# map(function, iterable) 
#       Applies a function to each value in an iterable.
#       Returns the data (generator) with the results of each value
#       passed into the function.

data = [1, 2, 3, 4, 5]

def square(x):
    # print("Received", x)
    # print("Returning", x ** 2)
    return x ** 2

squares = map(square, data)

# print(data)
# print(squares)


# filter(function, iterable)
#      

numbers = [5, 18, 7, 9, 14, 6, 1]

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

results = list(filter(is_even, numbers))

# print(numbers)
# print(results)



# reduce(function, iterable, initial)
#      

numbers = [1, 2, 3, 4, 5]

def f(a, b):
    print("Received: a=", a, ", b=", b, sep="")
    return a + b

# result = reduce(f, numbers)
# print("Result", result, type(result))



sentence = "Hello there world! Python is wonderful!"
vowels = "aeiou"

def f(a, b):
    print("Received: a=", a, ", b=", b, sep="")
    if not b in vowels:
        return a + b
    else:
        return a

result = reduce(f, sentence)
print(result)








# Higher order function recode


# map

def map(function, values):
    print("Running my map!!!")
    new_values = []
    for value in values:
        v = function(value)
        new_values.append(v)
    return new_values

values = list("abcsajhdfjdf")
function = str.upper

new_values = map(function, values)
new_values = map(str.upper, values)

print(values)
print(new_values)


# filter

def filter(function, values):
    print("My filter")
    new_values = []
    for value in values:
        if function(value) == True:
            new_values.append(value)
    return new_values


def is_even(number):
    return number % 2 == 0

numbers = [6,4,8,43,43,78,4,23,5]

output = filter(is_even, numbers)

print(numbers)
print(output)



# reduce


def reduce(function, values):
    accumulator, *values = values
    for value in values:
        v = function(accumulator, value)
        accumulator = v
        # print(f"{accumulator = }")
    return accumulator

from random import randint
from operator import add

numbers = [randint(2, 50) for _ in range(10)]

print(numbers)
total = reduce(add, numbers)
print(total)

def smaller(a, b):
    if a > b:
        return a
    else:
        return b

print(numbers)
answer = reduce(smaller, numbers)
print(answer)
