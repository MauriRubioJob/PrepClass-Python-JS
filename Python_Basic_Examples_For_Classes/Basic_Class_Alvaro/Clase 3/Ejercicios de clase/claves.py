
listado = [('e', '?'), ('a', '-'), ('c', '/'), ('d', '@')]

clave = input('Dime una clave: ')

def _transformar(valor, encript=True):
    a = 10 if encript else 5

    for item in listado:
        if encript:
            valor = valor.replace(item[0], item[1])
        else:
            valor = valor.replace(item[1], item[0])
    return valor

print(_transformar(clave))

print(locals())