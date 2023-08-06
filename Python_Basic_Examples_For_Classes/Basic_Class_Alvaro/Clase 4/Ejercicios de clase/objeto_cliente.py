
class Cliente:
    nombre = ''
    apellido = ''
    edad = 0
    cuenta_bacaria = ''

    def __init__(self, nombre, edad, cuenta_bancaria):
        self.nombre = nombre
        self.edad = edad
        self.cuenta_bancaria = cuenta_bancaria

cantidad = int(input('CUantos??'))
lista_clientes = []
while cantidad > 0:
    nombre = input('NOmbre: ')
    edad = int(input('Edad: '))
    cuenta = input('cuenta')
    cliente = Cliente(nombre=nombre, edad=edad, cuenta_bancaria=cuenta)
    lista_clientes.append(cliente)
    cantidad -= 1

for cliente in lista_clientes:
    print(f'Nombre: {cliente.nombre} -------> {cliente.cuenta_bancaria}')