
class Alumno:
    nombre = ''
    dni = ''
    telefono = ''

    def __init__(self, dni='12323f'):
        self.dni = dni


a = Alumno(dni='13424sds')
a.nombre = 'juan'
print(a.nombre)

b = Alumno(dni='345245O')
b.nombre = 'elena'
print(b.nombre)
print(a.nombre)

print(a.dni)


print('------------------------------')

class Cliente:
    nombre = ''
    apellido = ''
    edad = 0
    cuenta_bancaria = ''

    def __init__(self, nombre, edad, cuenta_bancaria):
        self.nombre = nombre
        self.edad = edad
        self.cuenta_bancaria = cuenta_bancaria

a = Cliente('Juan', 15, '134134134134')
a.apellido = 'lll'

b = Cliente('Carmen', 23, '1341341341234123413')
b.apellido = 'lll'

if a.edad > b.edad:
    print(a.nombre)
else:
    print(b.nombre)

lista = [a, b]

for i in lista:
    print(i.nombre)