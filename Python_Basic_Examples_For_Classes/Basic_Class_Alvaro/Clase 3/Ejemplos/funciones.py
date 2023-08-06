def hola_mundo():
    print('Hola esto es una funcion')


hola_mundo()


def multiplicar(valor, valor_2=90):
    print(valor * valor_2)

multiplicar(10, 55)

numero = 100
numero_2 = 50

multiplicar(numero)


def sumar_numeros(lista):
    total = 0
    for i in lista:
        if i < 11:
            total += i

    print(total)

lista_numeros = [10, 5, 10, 8, 9, 55]

sumar_numeros(lista_numeros)


def agregar(lista, numero):
    lista.append(numero)
    print(lista)

agregar(lista_numeros, 'hola mundio')

print(lista_numeros)