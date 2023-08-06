

texto = 'hola mi mundo es xxxxxxxxx.'

print(texto.startswith('Hola'))
print(texto.startswith('hola'))
print(texto.endswith('hola'))
print(texto.startswith('hola', 0, 10))

contenido = ' - '.join(['6623444', '1234123', '12341234'])
print(contenido)

print('234234-2342323-234234'.split('-'))

texto = 'El Mejor SISTEMA DEl MUNDO'

texto = texto.upper().replace('MEJOR', 'PEOR')
print(texto)
texto = texto.replace('DEL MUNDO', 'DE ESPAÑA').replace('PEOR', 'MEJOR').title()
print(texto)