
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


def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while right > left:
        midpoint = int((right - left) / 2) + left
        middle_name = data[midpoint]

        if middle_name == target:
            print("Found", target, "at position", midpoint)
            return midpoint
        elif middle_name < target:
            left = midpoint + 1
        elif middle_name > target:
            right = midpoint - 1


sorted_data = sorted(data)
binary_search(sorted_data, "Charlie")
