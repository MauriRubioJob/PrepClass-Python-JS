class Usuario:
    nombre = 'xxx'
    apellido = 'tttt'
    dni = '3333'

    def get_nombre(self):
        return self.nombre


class Alumno():
    telefonos = []

    def get_dni(self):
        return self.dni

    def get_nombre(self):
        return f'{self.nombre} {self.apellido}'

class Profesor(Usuario, Alumno):
    email = 'email'

# alumno = Alumno()
# print(alumno.nombre)
# print(alumno.apellido)
# print(alumno.dni)
# print(alumno.telefonos)
#
# print(alumno.get_nombre())
# print(alumno.get_dni())

profesor = Profesor()
print(profesor.email)
print(profesor.get_dni())

