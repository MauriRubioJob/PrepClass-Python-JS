import operator
import sys

operations = {
    "add": operator.add,
    "subtract": operator.sub,
    "multiply": operator.mul,
    "divide": operator.truediv,
}

filename = sys.argv[1]
with open(filename) as file:
    total = 0
    for line in file:
        a, operation, b = line.split()
        a, b = map(int, (a, b))
        total += operations[operation](a, b)
    print(f"Total = {total}")
