listado_coches = [
    {'matricula': 'edt234', 'marca': 'audi', 'color': 'verde', 'tipo': 'turismo', 'ano': '2009', 'costo': 4000},
    {'matricula': '988xvt', 'marca': 'toyota', 'color': 'azul', 'tipo': 'turismo', 'ano': '2015', 'costo': 24000},
    {'matricula': '889REW', 'marca': 'nissan', 'color': 'blanco', 'tipo': 'turismo', 'ano': '2019', 'costo': 38000},
]

listado_clientes = [
    {'nombre': 'Juan', 'dni': '234234J', 'email': 'jaun@a.com'},
    {'nombre': 'Elena', 'dni': '123456F', 'email': 'elena02@a.com'}
]


def agregar_coche(matricula, marca, color, tipo, ano, costo):
    coche = {
        'matricula': matricula,
        'marca': marca,
        'color': color,
        'tipo': tipo,
        'ano': ano,
        'costo': costo,
    }
    listado_coches.append(coche)


def registrar_coche():
    matricula = input('Matricula del coche: ')
    marca = input('Marca del coche: ')
    color = input('Color del coche: ')
    ano = input('Año del coche: ')
    costo = int(input('Costo del coche: '))
    tipo = input('Tipo de coche: ')
    if matricula_valida(matricula) is False:
        matricula = '000XXX'
    agregar_coche(matricula, marca, color, tipo, ano, costo)


def matricula_valida(matricula):
    if len(matricula) == 6 and str(matricula[0:3]).isdigit() and str(matricula[3:]).isalpha():
        return True
    return False


# registrar_coche()
def agregar_cliente(nombre, dni, email):
    listado_clientes.append({'nombre': nombre, 'dni': dni, 'email': email})


def registrar_cliente():
    nombre = input('Nombre: ')
    dni = input('DNI: ')
    email = input('Email: ')
    agregar_cliente(nombre, dni, email)

compras = []

def busqueda(listado, key, valor):
    for item in listado:
        if valor == item[key]:
            return True
    return False


def compra(dni, matricula, monto):
    if busqueda(listado_clientes, 'dni', dni) and busqueda(listado_coches, 'matricula', matricula):
        compras.append({'dni': dni, 'matricula': matricula, 'monto': monto})

compra('234234J', '988xvt', 2344)
print(compras)
# registrar_cliente()
# print(listado_clientes)
