adding_to_end = "Add 'e' to the end of the list."
print(adding_to_end)
x = ["a", "b", "c", "d"]


x.append("e")
print(x)


################################################################################


adding_to_beginning = "Add 'a' to the beginning of the list."
print(adding_to_beginning)
x = ["b", "c", "d", "e"]


x.insert(0, "a")
print(x)


################################################################################


removing_from_position = "Remove the 3rd name from the list."
print(removing_from_position)
x = ["Arthur", "Bill", "Charlie", "Dobby", "Errol", "Fred"]


x.pop(2)
print(x)


################################################################################


removing_by_value = "Remove the 'Fred' from the list."
print(removing_by_value)
x = ["Arthur", "Bill", "Charlie", "Dobby", "Errol", "Fred"]


x.remove("Fred")
print(x)


################################################################################


sorting = "Sort the list in descending order."
print(sorting)
x = [6, 8, 14, 11, 4, 1, 20]


x.sort(reverse=True)
x = sorted(x, reverse=True)
print(x)


################################################################################


finding_maximum = "Find the maximum value in the list."
print(finding_maximum)
x = [33.98, 80.41, 1.04, 45.12, 53.88, 26.84]


print(max(x))


################################################################################


finding_minimum = "Find the minimum value in the list, using a different method to how you found the maximum."
print(finding_minimum)
x = [31.02, 32.37, 96.97, 83.64, 11.99, 65.63]


x.sort()
print(x[0])


################################################################################


simple_indexing = "Print the 'd' from the list."
print(simple_indexing)
x = ["a", "b", "c", "d", "e"]

index = x.index("d")
print(x[index])

print(x[3])


################################################################################


multidimensional_indexing = "Print the letter 'o' from the data."
print(multidimensional_indexing)
x = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't']
]


inner_list = x[2]
print(inner_list[4])


################################################################################


multidimensional_adding = "This data holds names, eye colours, and ages. Take input from the user of 3 more people and add their records to the list."
print(multidimensional_adding)
x = [
    ["alice", "blue", 42],
    ["bob", "green", 33],
    ["charlie", "green", 19]
]

# for i in range(3):
#     name = input("Enter name: ")
#     eyecolour = input("Enter eye colour: ")
#     age = int(input("Enter age: "))
#     data = [name, eyecolour, age]
#     x.append(data)

# print(x)


################################################################################


characters_from_strings = "Seperate this string into a list of its individual characters."
print(characters_from_strings)
x = "Today is the 15th of Feburary."


# y = []
# for i in range(len(x)):
#     y.append(x[i])

# for character in x:
#     y.append(character)

# print(y)


y = list(x)
print(y)


################################################################################


string_from_a_list = "Combine the characters in this list into one string."
print(string_from_a_list)
x = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'n', 'o', '.', '1']


joined = ""
for i in range(len(x)):
    joined += x[i]

print(joined)


joined = "".join(x)
print(joined)
