import random


names = ["nico"]

operations = ["add", "subtract", "multiply", "divide"]

for name in names:
    with open(f"number_task/{name}_1", "w") as file:
        for _ in range(1000):
            a = random.randint(1, 999)
            operation = random.choice(operations)
            if operation in operations[2:]:
                b = random.randint(2, 20)
            else:
                b = random.randint(1, 999)
            file.write(f"{a} {operation} {b}\n")
