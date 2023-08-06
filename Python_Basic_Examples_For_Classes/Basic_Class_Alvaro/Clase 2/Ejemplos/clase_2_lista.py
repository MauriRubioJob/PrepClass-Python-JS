lista = [10, 30, 0, 11, 55, 14, 80, 42, 9, 66, 38, 10, 14, 25, 30]

print(lista)

# agregar 10, 5 , 2 a la lista

lista.append(10)
lista.append(5)
lista.append(2)

print(lista)

# Eliminar el penultimo elemento
penultimo = len(lista) - 2

lista.pop(penultimo)

print(lista)

# Imprimir el valor de los indices 3, 5, 8
print(lista[3])
print(lista[5])
print(lista[8])