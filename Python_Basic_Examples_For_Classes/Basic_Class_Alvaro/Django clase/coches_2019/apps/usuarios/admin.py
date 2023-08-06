from django.contrib import admin

from apps.usuarios.models import *

admin.site.register((Cliente, Empleados))