# Add for me

# Default imports
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    matricula = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    adquisicion = models.DateField()
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
                    
    def __str__(self):
        return self.marca
    
class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class DeteccionPlaca(models.Model):
    imagen_captura = models.ImageField(upload_to='capturas_anpr/')
    matricula_leida = models.CharField(max_length=100, blank=True, null=True)
    confianza = models.FloatField(null=True, blank=True)    # Fecha y hora exacta en la que pasó el vehículo
    fecha_hora = models.DateTimeField(auto_now_add=True)
    auto_registrado = models.ForeignKey(Auto, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Detección: {self.matricula_leida} - {self.fecha_hora}"