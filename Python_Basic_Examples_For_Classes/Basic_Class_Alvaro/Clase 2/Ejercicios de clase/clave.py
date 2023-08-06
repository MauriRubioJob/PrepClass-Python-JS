
clave = 'miclave12377ssjn'


lista = [
    ('m', '?'),
    ('i', '%'),
    ('c', ')'),
    ('1', '¿'),
    ('7', '@'),
    ('s', '-'),
]

for item in lista:
    clave = clave.replace(item[0], item[1])

print(clave)


for item in lista:
    clave = clave.replace(item[1], item[0])

print(clave)