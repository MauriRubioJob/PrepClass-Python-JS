from django.db import models

from apps.coches.models import Coche
from apps.usuarios.models import Cliente

ESTADO_PAGOS = (
    (1, 'Pagado'),
    (2, 'Confirmando Pago'),
    (3, 'Cancelado')
)


class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.IntegerField(choices=ESTADO_PAGOS)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)