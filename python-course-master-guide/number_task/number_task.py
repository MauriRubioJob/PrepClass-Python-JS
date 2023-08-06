# Find the answer to each calculation in the file, and
# then calulate the total of all 1000 answers.


filename = "number_task/nico_0"
file = open(filename, "r")
contents = file.read()
file.close()

print(type(contents))
print(len(contents))

# Break the one long string up into the individual lines
lines = contents.splitlines()

print(type(lines))
print(len(lines))

# Put the list of lines together with a for loop
# This will give us each line on at a time.
for line in lines:
    print("The line variable =", line)

    # Break the calculation up into the 3 parts
    parts = line.split()
    print(parts)

    a = int(parts[0])
    b = int(parts[2])
    answer = a + b
    print(answer)
