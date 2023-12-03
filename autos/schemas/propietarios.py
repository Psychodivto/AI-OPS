import graphene

from graphene_django.types import DjangoObjectType
from graphene import relay
from autos.models import Propietario, Auto

class AutoType(DjangoObjectType):
    class Meta:
        model = Auto
        fields = ("id", "marca", "modelo", "color", "matricula", "anio", "imagen_url")

class PropietarioType(DjangoObjectType):
    auto =  graphene.Field(AutoType)

    class Meta:
        model = Propietario
        fields = (
            "id",
            "nombre",
            "apellido",
            "fecha_nacimiento",
            "email",
            "telefono",
            "direccion",
        )

class PropietariosConnection(relay.Connection):
    class Meta:
        node = PropietarioType

class Query(graphene.ObjectType):
    all_propietarios = graphene.List(PropietarioType)
    nombre_propietario = graphene.Field(PropietarioType, nombre=graphene.String())
    telefono_propietario = graphene.Field(PropietarioType, telefono=graphene.String())

    def resolve_all_propietarios(self, info, **kwargs):
        return Propietario.objects.all()
        for propietario in propietarios:
            propietario.auto = propietario.auto.marca
        return propietarios

    def resolve_nombre_propietario(self, info, **kwargs):
        nombre = kwargs.get("nombre")
        if nombre is not None:
            return Propietario.objects.get(nombre=nombre)
        return None 
    
    def resolve_telefono_propietario(self, info, **kwargs):
        telefono = kwargs.get("telefono")
        if telefono is not None:
            return Propietario.objects.get(telefono=telefono)
        return None

class CreatePropietario(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    apellido = graphene.String()
    fecha_nacimiento = graphene.Date()
    telefono = graphene.String()
    email = graphene.String()
    direccion = graphene.String()

    class Arguments:
        nombre = graphene.String()
        apellido = graphene.String()
        fecha_nacimiento = graphene.Date()
        telefono = graphene.String()
        email = graphene.String()
        direccion = graphene.String()

    def mutate(self, info, nombre, apellido, fecha_nacimiento, telefono, email, direccion):
        propietario = Propietario(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, telefono=telefono, email=email, direccion=direccion)
        propietario.save()
        return CreatePropietario(
            id=propietario.id,
            nombre=propietario.nombre,
            apellido=propietario.apellido,
            fecha_nacimiento=propietario.fecha_nacimiento,
            telefono=propietario.telefono,
            email=propietario.email,
            direccion=propietario.direccion,
        )

class Mutation(graphene.ObjectType):
    create_propietario = CreatePropietario.Field()

schema = graphene.Schema(query=Query)


