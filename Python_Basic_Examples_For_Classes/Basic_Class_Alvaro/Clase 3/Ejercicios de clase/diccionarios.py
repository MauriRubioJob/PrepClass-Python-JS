persona = {
    'nombre': 'Juan',
    'edad': 45,
    'telefonos': ('3453455', '34534534'),
    'dni': '2345245X'
}

print(persona)

print(f'el nombre es: {persona["nombre"]}')
print(f'el edad es: {persona["edad"]}')
print(f'el dni es: {persona["dni"]}')
print(f'los telefonos son: {" - ".join(persona["telefonos"])}')

# Limpiar un diccionario
# persona.clear()
persona_2 = {'nombre': 'Elena', 'email': 'elena033@email.com'}
print(persona)
print(persona_2)
persona.update(persona_2)
print(persona)

print(persona.get('nombre'))
print(persona.get('apellido', 'mi apellido'))

print(persona_2.keys())
print(persona_2.values())
print(persona_2.items())

print(persona)
persona['apellido'] = 'XXXXXXXXXXX'
print(persona)