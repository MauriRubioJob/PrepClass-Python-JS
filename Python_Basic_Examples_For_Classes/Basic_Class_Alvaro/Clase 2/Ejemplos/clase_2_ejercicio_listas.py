
clientes = [['Javi', 21, 100, (6630812,)], ['Elena', 30, 600, (6681516, 6620013)], ['Carlos', 42, 550, ()]]

for cliente in clientes:
    if len(cliente[3]) == 0:
        print(f'Nombre: {cliente[0]} - Edad: {cliente[1]} - Telefono: No tiene')
    else:
        print(f'Nombre: {cliente[0]} - Edad: {cliente[1]} - Telefono: {cliente[3][0]}')