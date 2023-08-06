
pi = 3.14159265
age = 42
name = "Bob"

# Horrible version
message = "'" + name + " is " + str(age) + " years old, and their favourite number is " + str(pi) + "'"


# Modulus formatting
#  %s == string
#  %d == integer
#  %f == float
message = "'%s is %f years old, and their favourite number is %f'" % (name, age, pi)


# Format function
message = "'{} is {} years old, and their favourite number is {}'".format(name, age, pi)
print(message)


# String literals
age_calc = 99 / 2 + 100 * 4 /1000 **2
message = f"'{name} is {age_calc} years old, and their favourite number is {pi:.1f}'"
print(message)
