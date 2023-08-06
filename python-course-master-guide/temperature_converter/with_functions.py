def celcius_to_fahrenheit(celcius):
    fahrenheit = celcius * (9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * (5 / 9)
    return celcius


print("Convert from Celcius (c) or Fahrenheit (f)?   c/f")
unit = input("> ")

if unit == "c":
    print("Enter a temperature in Celcius:")
    celcius = float(input("> "))
    fahrenheit = celcius_to_fahrenheit(celcius)
    print(celcius, "ºC is", fahrenheit, "ºF")

elif unit == "f":
    print("Enter a temperature in Fahrenheit:")
    fahrenheit = float(input("> "))
    celcius = fahrenheit_to_celcius(fahrenheit)
    print(fahrenheit, "ºF is", celcius, "ºC")
