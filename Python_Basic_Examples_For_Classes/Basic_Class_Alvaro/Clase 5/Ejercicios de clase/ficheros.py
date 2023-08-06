nombre = 'juan'
dni = '123123H'

fichero = open('fichero.txt', 'w+')
fichero.write(f'{nombre}, {dni}\n')
fichero.close()

with open('fichero.txt', 'r') as mi_fichero:
    contenido = mi_fichero.readlines()
    print(contenido)
    contenido_2 = mi_fichero.readline()
    print(contenido_2)