import graphene
from graphene_django import DjangoObjectType
from sistema.models import Auto, Propietario

class AutoType(DjangoObjectType):
    class Meta:
        model = Auto
        fields = ("id", "marca", "modelo", "anio", "matricula", "color", "adquisicion", "imagen_matricula")
        
class PropietarioType(DjangoObjectType):
    class Meta:
        model = Propietario
        fields = ("id", "nombre", "apellido", "dni", "direccion", "telefono", "email", "auto")
        