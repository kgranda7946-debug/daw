from django.contrib import admin

from manejo_seguros.models import Employe, Type, Cliente, TypeSeguro, Aseguradadora, Poliza

# Register your models here.

admin.site.register(Employe)
admin.site.register(Type)
admin.site.register(Cliente)
admin.site.register(TypeSeguro)
admin.site.register(Aseguradadora)
admin.site.register(Poliza)
