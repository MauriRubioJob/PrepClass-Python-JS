tupla = (10, 12, 0, 15, 30, 18)

for item in tupla:
    if item > 12:
        print(f'La edad del usuario es: {item}')
    # if 15 < item < 30:
    #     print('El usuario es mayor que 15 y menor a 30')

    if item > 15 and item < 30:
        print('El usuario es mayor que 15 y menor a 30')

    if item > 0 or item < 15:
        print('Es mayor que 0 y menor que 15')

# La edad del usuario es: EDAD

