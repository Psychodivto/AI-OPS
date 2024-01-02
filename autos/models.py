from django.db import models

# Create your models here.
    

class Propietario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=True)
    telefono = models.CharField(max_length=10, verbose_name="Telefono")
    email = models.EmailField(max_length=100, verbose_name="Email")
    direccion = models.TextField(blank=True, verbose_name="Direccion")

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def __str__(self):
        return self.nombre_completo()


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

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ["nombre"]
        verbose_name = "Marca"
        db_table = "marcas"

class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, verbose_name="Marca")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, null=True, verbose_name="Propietario")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    color = models.CharField(max_length=100, verbose_name="Color")
    matricula = models.ImageField(upload_to="images/", null=True)
    anio = models.PositiveIntegerField(verbose_name="Año de fabricacion", null=True)
    adquisicion = models.DateField(verbose_name="Fecha de adquisicion", null=True)
    imagen_url = models.TextField(blank=True, verbose_name="Url de la imagen")
    # related_name='autos'
    
    def __str__(self):
        return self.modelo
    
    class Meta:
        ordering = ["modelo"]
        verbose_name = "Auto"
        db_table = "autos"
