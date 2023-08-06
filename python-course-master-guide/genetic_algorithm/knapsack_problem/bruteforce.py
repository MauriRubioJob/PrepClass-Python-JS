import item_reader
import itertools
import timeit
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def get_value(item):
    return item[1]


def get_total_value(items):
    total_value = 0
    for item in items:
        total_value += item[1]
    return total_value


def get_total_volume(items):
    total_volume = 0
    for item in items:
        total_volume += item[2]
    return total_volume


def bruteforce(items):
    start_time = timeit.default_timer()
    # print("Started calculating combinations at", start_time)

    combinations = []
    for i in range(1, len(items) + 1):
        combs = list(itertools.combinations(items, r=i))
        for x in combs:
            combinations.append(x)
    # print("Total combinations found:", len(combinations))

    valid_combinations = []
    for combination in combinations:
        total_volume = get_total_volume(combination)
        if total_volume <= 100:
            valid_combinations.append(combination)
    # print("Valid combinations:", len(valid_combinations))

    valid_combinations.sort(key=get_total_value, reverse=True)
    in_suitcase = valid_combinations[0]

    end_time = timeit.default_timer()
    time_taken = round((end_time - start_time) * 1000, 3)
    # print("Finished at", end_time)
    print("Took", time_taken, "ms")

    print("Found best. Total value:", get_total_value(in_suitcase),
          "Total volume:", get_total_volume(in_suitcase))
    for item in in_suitcase:
        print(item[0], end=", ")


if __name__ == "__main__":
    items = item_reader.read(amount=20)
    bruteforce(items)
