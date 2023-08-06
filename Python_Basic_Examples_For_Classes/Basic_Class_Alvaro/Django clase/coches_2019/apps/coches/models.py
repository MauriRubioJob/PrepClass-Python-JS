from django.db import models

from apps.usuarios.models import Cliente

ESTADOS = (
    ('A', 'Activo'),
    ('E', 'Eliminado')
)

TIPOS_MARCAS = (
    'A', 'Automatico',
    'D', 'Deportivo',
    '4', '4 X 4',
)


class Marca(models.Model):
    nombre = models.CharField(max_length=25)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    estado = models.CharField(max_length=1, choices=ESTADOS)

    def __str__(self):
        return self.nombre


class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    ano = models.DateField()
    tipo = models.CharField(max_length=1)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Coche(models.Model):
    ano = models.DateField()
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, blank=True, null=True)
    matricula = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    propietario = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.matricula