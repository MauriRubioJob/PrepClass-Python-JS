
def read(amount):
    with open("items_with_values", "r") as file:
        items = []
        for i, line in enumerate(file.read().splitlines()):
            if i >= amount:
                return items
            things = line.split(",")
            name = things[0]
            value = int(things[1])
            volume = int(things[2])
            weight = float(things[3])
            item = name, value, volume, weight
            items.append(item)
            if i >= amount:
                return items
