import random

def generate():
    with open("items", "r") as file_in:
        with open("items_with_values", "w") as file_out:
            for name in file_in:
                value = random.randint(1, 100)
                volume = random.randint(5, 20)
                weight = round(random.random() * 10, 2)
                item = f"{name.strip()},{value},{volume},{weight}\n"
                file_out.write(item)


def create():
    items = []
    for i in range(26):
        for j in range(26):
            name = chr(65+i) + chr(65+j)
            value = random.randint(1, 100)
            volume = round(random.random() * 5 + 1, 2)
            weight = round(random.random() * 10, 2)
            item = name, value, volume, weight
            items.append(item)
    return items
