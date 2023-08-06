
names = ["Arthur", "Bill", "Charlie", "Fred", "George",
    "Ginny", "Harry", "Hermione", "Molly", "Percy", "Ron", "Voldemort"]

number_of_names = len(names)
longest_name = len(max(names, key=len))


for i in range(0, number_of_names - 1, 3):
    name_a = names[i]
    name_b = names[i+1]
    name_c = names[i+2]


    formatted_string = "{:<20}{:<20}{:<20}".format(name_a, name_b, name_c)
    print(formatted_string)

