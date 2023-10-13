from django.db import models


# Create your models here.

class Propietario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    telefono = models.CharField(max_length=100, verbose_name="Telefono")
    email = models.EmailField(max_length=100, verbose_name="Email")
    direccion = models.TextField(blank=True, verbose_name="Direccion")

    def nombre_completo(self):
        return self.nombre + ' ' + self.apellido

    def __str__(self):
        return self.nombre

class Meta:
    ordering = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'email', 'direccion']
    Verbose_name = "Propietario"
    Verbose_name_plural = "Propietarios"
    db_table = "propietario"
 
class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    matricula = models.IntegerField(max_length=100)
    ano = models.IntegerField(max_length=5)
    imagen_url = models.TextField(blank=True) 
    propietario = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE, ) #related_name='autos'

    def __str__(self):
        return self.marca
