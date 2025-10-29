from django.db import models
from datetime import datetime
# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tipo de empleado')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre de Categoria')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'

class Employe(models.Model):
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type,on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=150, verbose_name='Nombre')
    email = models.EmailField(max_length=100, verbose_name='Correo electronico')
    address = models.TextField(max_length=300, verbose_name='Dirección')
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Salario')
    avatar = models.ImageField(upload_to='avatar', verbose_name='Imagen',null=True, blank=True)
    cv = models.ImageField(upload_to='vitae',verbose_name='Curriculum Vitae', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'

class Granda(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Apellidos'
        verbose_name_plural = 'Apellidos'
        db_table = 'apellido'


class Kliuwher(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.EmailField(max_length=100, verbose_name='Correo electronico')
    Direcion = models.CharField(max_length=40, verbose_name='Direcion')
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    id_pais = models.ForeignKey(Granda, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Nombre'
        verbose_name_plural = 'Nombres'
        db_table = 'nombre'

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    identificacion = models.CharField(max_length=50, unique=True, verbose_name='Identificacion')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    email = models.EmailField(max_length=100, verbose_name='Correo electronico')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    telefono = models.CharField(max_length=50, verbose_name='Telefono')
    avatar = models.ImageField(upload_to='avatar', verbose_name='Imagen',null=True, blank=True)
    cv = models.FileField(upload_to='vitae',verbose_name='Curriculum Vitae', null=True, blank=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'

class TypeSeguro(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre')
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Seguro'
        verbose_name_plural = 'Seguros'
        db_table = 'seguro'

class Aseguradadora(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name='Nombre')
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Aseguradadora'
        verbose_name_plural = 'Aseguradados'
        db_table = 'aseguradadora'

class Poliza(models.Model):
    numPoliza = models.CharField(unique=True, max_length=50, verbose_name='Poliza')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    cliente =models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    type_Seguro = models.ForeignKey(TypeSeguro, on_delete=models.CASCADE, null=True)
    Aseguradora = models.ForeignKey(Aseguradadora, on_delete=models.CASCADE, null=True)
    fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    fecha_fin = models.DateField(verbose_name='Fecha de fin')
    valor_seguro = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Valor del seguro')
    valor_prima =models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Valor Prima')
    valor_adicional = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Valor Adicional')
    def __str__(self):
        return self.numPoliza
    class Meta:
        verbose_name = 'Poliza'
        verbose_name_plural = 'Polizas'
        db_table = 'poliza'