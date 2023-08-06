usuario = {
    'nombre': 'Juan',
    'edad': 25,
    'dni': '93178422Y',
    'telefono': [663558874, 663418004],
    'hijos': [],
    'empresa_actual': {
        'nombre': 'ING',
        'años': 1,
        'sueldo': 2500,
    },
    'trabajos': [
        {
            'empresa': 'HP',
            'años': 2,
            'sueldo': 1500,
        },
        {
            'empresa': 'Google',
            'años': 10,
            'sueldo': 2000,
        }
    ]
}

"""
    1) Crear una funcion que retorne el nombre del usuario
    2) Crear una funcion que retorne los años que trabajo en sus trabajos anteriores
    3) Crear una funcion que retorne la suma de los años que trabajo en sus trabajos anterior + el actual
    4) Crear una funcion que returne la suma lo que ha ganado (Ejemplo años en la empresa 1 * sueldo) esta operacion
    se  tiene que repetir por cada trabajo incluyendo el actual para obtener un total y retornarlo
    5) Crear una funcion que agrege hijos
    6) Agregar los siguientes hijos (Juan 13 años, Maria 16, Julieta 2)
    7) Agregar un nuevo elemento al diccionario usuario que sea esposa y tengo un diccionario con 
    {'nombre': 'Petra', 'edad':26}
    8) Agregar una lista [] basia de telefonos al diccionario esposa que fue agregado al usuario en el paso anterior
    9) Crear una funcion que agregue telefonos a una lista
    10) Usando la funcion anterior agregar el siguiente telefono 603345890
"""