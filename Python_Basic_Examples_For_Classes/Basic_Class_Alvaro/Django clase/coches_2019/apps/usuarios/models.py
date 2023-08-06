from django.core.exceptions import ValidationError
from django.db import models

TIPO_CHOICES = {
    ('a', 'Admin'),
    ('v', 'Vendedor'),
}

def x(value):
    pass

def validador_dni(value):
    if not str(value[0]).isalpha() and not str(value[-1]).isalpha():
        raise ValidationError('No se cumple la validacion')


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=10, validators=[validador_dni])
    email = models.EmailField()
    direccion = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.nombre.title()} {self.apellido.title()}'


def validar_clave(value):
    if len(value) < 6 or ['@', '#', ';', ',', '?'] not in value or not str(value[-1]).isupper():
        raise ValidationError('La contraseña no cumple con los requerimientos')

class Empleados(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    clave = models.CharField(max_length=30, validators=[validar_clave])
    telefono = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.email
