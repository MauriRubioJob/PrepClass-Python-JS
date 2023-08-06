CURSO_1 = 'curso_01'
CURSO_2 = 'curso_02'
CURSO_3 = 'curso_03'
CURSO_4 = 'curso_04'
CURSO_5 = 'curso_05'


class Usuario(object):
    username = ''
    clave = ''


class Persona(object):
    nombre = ''
    apellido = ''
    edad = 0
    telefonos = []
    correos = []

    def agregar_telefono(self, telefono):
        self.telefonos.append(str(telefono))

    def agregar_correos(self, correo):
        self.correos.append(str(correo))


class Asignatura(object):
    nombre = ''
    cursos = []

    def agregar_curso(self, curso):
        # Agrega un curso a la asignatura
        self.cursos.append(curso)

    def validar_curso(self, curso):
        # Retorna True si la asignatura pertenece a un curso
        return self.cursos.count(curso)


class Almunno(Persona):
    usuario = Usuario()
    curso = ''
    asignaturas = []

    def agregar_asignatura(self, asignatura):
        # Comprobamos que la asignatura se puede agregar al curso y la agregamos
        if asignatura.validar_curso(self.curso):
            self.asignaturas.append(asignatura)
            return True
        else:
            return False

    def get_nombre(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def nombre_usuario(self):
        return self.usuario.username



# Creamos un Usuario
usuario_1 = Usuario()
usuario_1.username = 'Usuario_1'
usuario_1.clave = '=123456789.?¿'

# Creamos un Alumno
alumno_1 = Almunno()
alumno_1.usuario = usuario_1
alumno_1.nombre = 'Pedro'
alumno_1.apellido = 'Federico'
alumno_1.agregar_telefono('1234587')
alumno_1.curso = CURSO_2
alumno_1.agregar_correos('micorreo@correos.es')

# Creamos una asignatura
matematica = Asignatura()
matematica.nombre = 'Matematica'
matematica.agregar_curso(CURSO_1)
matematica.agregar_curso(CURSO_2)

# Agregamos matematica al alumno_1
alumno_1.agregar_asignatura(matematica)
"""
    El metodo anterior solo asigna una asignatura, pero para ser mas eficiente tendria que aceptar una lista de 
    asignaturas. Modifiquen el codigo y adaptelon para que esto sea posible.
    Este ejercicio no va a ser evaluado.
"""


print(alumno_1.get_nombre())
print(alumno_1.nombre_usuario())
for asignatura in alumno_1.asignaturas:
    print('El alumno: {} tiene la asignatura: {}'.format(alumno_1.nombre, asignatura.nombre))