lista_3 = [10, 5, 3, 4, 30]

x = 0
while x < len(lista_3):
    if x != 0:
        print(f'actual: {lista_3[x]} - anterior: {lista_3[x-1]}')
        if lista_3[x] > lista_3[x-1]:
            lista_3.insert(x-1, lista_3[x])
    else:
        print(f'actual: {lista_3[x]} inicio: {lista_3[x]}')
    x += 1

print(lista_3)