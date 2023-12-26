from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class Propietario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    telefono = models.CharField(max_length=10, verbose_name="Telefono")
    email = models.EmailField(max_length=100, verbose_name="Email")
    direccion = models.TextField(blank=True, verbose_name="Direccion")

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def __str__(self):
        return self.nombre


class Meta:
    ordering = [
        "nombre",
        "apellido",
        "fecha_nacimiento",
        "telefono",
        "email",
        "direccion",
    ]
    verbose_name = "Propietario"
    db_table = "propietarios"


class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    matricula = models.ImageField(upload_to="images/", null=True, blank=True)
    anio = models.IntegerField()
    imagen_url = models.TextField(blank=True)
    propietario = models.ForeignKey(
        Propietario, on_delete=models.CASCADE, null=True
    )  # related_name='autos'

    def __str__(self):
        return self.marca

class Meta:
    ordering = ["marca", "modelo", "color", "matricula", "anio", "imagen_url"]
    verbose_name = "Auto"
    db_table = "autos"


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    direccion = models.CharField(blank=True, max_length=255, null=True, verbose_name="Direccion")
    
