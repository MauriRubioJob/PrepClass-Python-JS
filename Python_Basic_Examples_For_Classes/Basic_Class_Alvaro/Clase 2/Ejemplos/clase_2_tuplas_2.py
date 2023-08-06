edades = (10, 15, 30, 18, 17, 8, 82, 55, 20, 21)

# Imprmir cuantos son mayores a 18

total = 0
for item in edades:
    if item > 18:
        total += 1
print(total)

# Imprimir '* ES MENOR DE EDAD *' si es menor a 18

for item in edades:
    if item < 18:
        print(f' ES MENOR DE EDAD {item}'.center(150, '*'))

# Imprimir la suma de todas las edades

total = 0
for item in edades:
    total += item

print(total)

# Imprimir la suma de los mayores a 10 y menores 55 y diferentes a 17 y 21
total = 0
for item in edades:
    if item > 10 and item < 55 and (item != 17 or item != 21):
            total += item

print(total)