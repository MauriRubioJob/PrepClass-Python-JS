alumnos = [
    {
        'nombre': 'Juana',
        'dni': '2345234P'
    },
    {
        'nombre': 'Pedro',
        'dni': '23423452X'
    }
]

for alumno in alumnos:
    print(f'El nombre del alumno es: {alumno["nombre"]} y su DNI es: {alumno["dni"]}')