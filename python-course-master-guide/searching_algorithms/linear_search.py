
data = [
    "Harry",
    "Ron"
    "Hermione",
    "Fred",
    "George",
    "Bill",
    "Ginny",
    "Charlie",
    "Percy",
    "Arthur",
    "Molly",
]


def linear_search(data, target):
    for i in range(len(data)):
        item = data[i]
        if item == target:
            print("Found", target, "at position", i)


linear_search(data, "Charlie")
