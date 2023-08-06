clientes = [
    {
        'nombre': 'Carmen',
        'codigo': '001',
        'email': 'carme01@xx',
        'monto': 250,
        'edad': 32,
    },
    {
        'nombre': 'Jose',
        'codigo': '003',
        'email': 'jo_01@xx',
        'monto': 1500,
        'edad': 45,
    },
    {
        'nombre': 'Maria',
        'codigo': '008',
        'email': 'maria@xx',
        'monto': 550,
        'edad': 28,
    }
]

div = ''.center(120, '-')

print('CLIENTES'.center(120, ' '))
for cliente in clientes:
    print(div)
    print(f'Cliente N {cliente["codigo"]}')
    print(div)
    print(f'Nombre: {cliente.get("nombre")}')
    print(f'Apellido: {cliente.get("apellido", "")}')
    print(f'Email: {cliente.get("email")}')
    print(f'Edad: {cliente.get("edad")}')
    print(f'Monto: {cliente.get("monto")} ---> Monto + 21 % I.V.A = {cliente.get("monto") * 1.21}')

codigos = ['003', '010', '008', '020']

for cliente in clientes:
    if cliente.get('codigo') in codigos:
        cliente['monto'] = cliente['monto'] - cliente['monto'] * 0.15

# print(clientes)
listado_clientes = []
for cliente in clientes:
    if cliente.get('monto') < 1000:
        tupla = (cliente.get('codigo'), cliente.get('email'), cliente.get('monto'))
        listado_clientes.append(tupla)

print(listado_clientes)