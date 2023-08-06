print(' Mi Sistema '.center(100, '#'))

nombre = input('Dime tu nombre: ')
edad = input('Dime tu edad: ')
dni = input('Dime tu DNI: ')

print(f'Tu nombre es: {nombre.title()}')
print(f'Tu edad: {edad.zfill(3)}')
print(f'Tu DNI: {dni.upper()}')
print(''.center(100, '#'))