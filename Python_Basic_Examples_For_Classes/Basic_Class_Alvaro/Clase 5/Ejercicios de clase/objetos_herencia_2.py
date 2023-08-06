
class Vehiculo:
    nombre = ''
    marca = ''
    ruedas = ''
    precio = ''

    def get_marca(self):
        print(self.marca)

class Coche(Vehiculo):
    puertas = 0

    def get_puertas(self):
        print(self.puertas)

    def get_marca(self):
        print(f'La marca del coche es: {self.marca}')

class Moto(Vehiculo):
    radio = True

    def get_radio(self):
        print(self.radio)

    def get_marca(self):
        print(f'La marca de la moto es: {self.marca}')


string = 'esto es un string'
print(dir(string))

