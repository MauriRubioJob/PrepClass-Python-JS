from django.contrib import admin
from django.utils.html import format_html

from apps.coches.models import *
from apps.pagos.models import *

admin.site.register((Modelo, Marca))

admin.site.site_header = 'VENDE TU COCHE.COM'


class CocheAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'ano', 'precio', 'estado_de_pago', 'cliente')

    def estado_de_pago(self, obj):
        pagos = Pago.objects.filter(coche=obj, estado=1)
        total = 0
        for pago in pagos:
            total += pago.cantidad

        return total

    def cliente(self, obj):
        pagos = Pago.objects.filter(coche=obj, estado=1)
        if pagos:
            return f'{pagos[0].cliente.nombre} {pagos[0].cliente.apellido}'
        return 'El coche no se ha comprado'

admin.site.register(Coche, CocheAdmin)
