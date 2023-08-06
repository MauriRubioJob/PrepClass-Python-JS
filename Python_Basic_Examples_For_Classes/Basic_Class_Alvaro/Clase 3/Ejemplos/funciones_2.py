clientes = [
    {'nombre': 'juan', 'edad': 24, 'monto': 23000},
    {'nombre': 'elena', 'edad': 32, 'monto': 17800},
]


def calcular_impuesto(monto):
    print(monto * 1.25)


for cliente in clientes:
    calcular_impuesto(cliente['monto'])

"""
a = &
c = )
d = /
o = $
e = !
0 = -
1 = ¿
2 = *
3 = =
4 = @
5 = #
|
len min = 6
"""


def encri(clave, long=6):
    if len(clave) < long:
        print('Error la clave es un pequeña')
    else:
        caracteres = (('4', '@'), ('3', '='), ('5', '#'))

        for caracter in caracteres:
            clave = clave.replace(caracter[0], caracter[1])
    return clave


"""
nombre
apellido
dni
edad
sexo
clave
"""


def registro(nombre, apellido, dni, edad, sexo, clave):
    nombre = str(nombre).title()
    apellido = str(apellido).title()
    dni = str(dni).upper()
    edad = int(edad)
    sexo = str(sexo).upper()

    resultado = f'{nombre} {apellido}, edad: {edad}, sexo: {sexo}, clave: {encri(clave)}'

    return resultado

"""
###########################
##### NOMBRE DE SISTEMA ###
###########################
"""


def head(texto):
    print('#' * 120)
    print(f'  {texto.upper()}  '.center(120, '#'))
    print('#' * 120)


def menu_option():
    print("""
        1 - Resgistrar
        2 - Ver Clave
        3 - Salir
        """)


def menu():
    menu_option()

    opt = input('Seleccionar: ')

    while opt != '3':
        if opt == '1':
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            edad = input('Edad: ')
            dni = input('DNI: ')
            sexo = input('Sexo: ')
            clave = input('clave')
            a = registro(edad=edad, nombre=nombre, apellido=apellido,
                     dni=dni, sexo=sexo, clave=clave)
            print(a)
            menu_option()
            opt = input()
        elif opt == '2':
            print('ver clave')
            menu_option()
            opt = input()
        else:
            print('opt no valida')
            opt = input()


menu()
