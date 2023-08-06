
alumnos = [('Juan', 17), ('Elena', 21), ('Ana', 25), ('Pedro', 18)]


for alumno in alumnos:
    print(f'El alumno {alumno[0]} tiene una edad de: {alumno[1]}')

    # Ejemplo de un for dentro de otro for
    for item in alumno:
        print(item)


print(''.center(150, '='))

clientes = [['Javi', 21, 100], ['Elena', 30, 600], ['Carlos', 42, 550]]

print(clientes)
# agragar mas listas a la lista
clientes.append(['Carmen', 33, 220])
clientes.append(['Roman', 29, 189])

print(clientes)

for cliente in clientes:
    print(f'El cliente {cliente[0]} tiene una deuda de: {cliente[2]}')