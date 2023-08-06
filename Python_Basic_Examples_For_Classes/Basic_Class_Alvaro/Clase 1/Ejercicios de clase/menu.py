print(' MENU '.center(100, '#'))

print("""
1 - Registro
2 - Imprimir datos
3 - Salir
""")

opt = '0'

while opt != '3':
    opt = input('opcion: ')
    if opt == '1':
        print('Registrado')
        # opt = '3'
    if opt == '2':
        print('Tus datos')
        # opt = '3'
print(' Fin')