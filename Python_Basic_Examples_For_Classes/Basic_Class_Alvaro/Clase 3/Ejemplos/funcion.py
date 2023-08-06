def operacion(valor_1, valor_2, operacion):
    if operacion == '*':
        return valor_1 * valor_2
    elif operacion == '+':
        return valor_1 + valor_2
    else:
        return valor_1 - valor_2

a = operacion(11, 5, '*')

# print(a/2)
"""
    [0, 0, 0, 0]
    [0, 0, 0, 0]
"""

def generar_lista(valor_1, valor_2, valor_3):
    lista = []
    for i in range(0, valor_1):
        lista_2 = []
        for x in range(0, valor_2):
            lista_2.append(valor_3)
        lista.append(lista_2)
    return lista

lista = generar_lista(5, 5, '0')

for item in lista:
    print(item)