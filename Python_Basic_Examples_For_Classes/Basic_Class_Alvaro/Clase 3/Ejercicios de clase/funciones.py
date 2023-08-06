
def hola_mundo():
    print('Hola mundo!')

hola_mundo()


def sumar():
    return 100 * 600

print(sumar())


def multiplicar(valor):
    return valor * 300

print(multiplicar(200))
print(multiplicar(1500))
print(multiplicar(5000))

def calcular_impuesto(sueldo, impuesto):
    return sueldo * (impuesto / 100)

print(calcular_impuesto(2500, 25))
print(calcular_impuesto(5800, 35))

lista_de_codigos = []

def agregar_codigo(codigo):
    lista_de_codigos.append(codigo)

agregar_codigo(100)
agregar_codigo(140)
agregar_codigo(600)

print(lista_de_codigos)

def years(inicio, fin):
    lista = []
    while inicio <= fin:
        lista.append(inicio)
        inicio += 1
    return lista

print(years(1998, 2000))