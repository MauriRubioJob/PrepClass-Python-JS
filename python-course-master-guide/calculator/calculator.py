
print("Welcome to the PyCalculator v1.0")
print("Enter your two numbers:")
number_a = float(input())
number_b = float(input())

print("Which operation would you like to perform? + - * /")
operation = input()


if operation == "+":
    answer = number_a + number_b
elif operation == "-":
    answer = number_a - number_b
elif operation == "*":
    answer = number_a * number_b
elif operation == "/":
    answer = number_a / number_b
else:
    print("Invalid operation.")

print("Answer:", answer)
