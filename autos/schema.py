import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay
from .models import Auto, Propietario

class AutoType(DjangoObjectType):
    class Meta:
        model = Auto
        fields = ("id", "marca", "modelo", "color", "matricula", "ano", "imagen_url")
class PropietarioType(DjangoObjectType):
    class Meta:
        model = Propietario
        fields = ("id", "nombre", "apellido", "fecha_nacimiento", "email", "telefono", "direccion")
class AutosConnection(relay.Connection):
    class Meta:
        node = AutoType
class PropietariosConnection(relay.Connection):
    class Meta:
        node = PropietarioType
class Query(graphene.ObjectType):
    all_autos = graphene.List(AutoType)
    all_propietarios = graphene.List(PropietarioType)

    def resolve_all_autos(self, info, **kwargs):
        return Auto.objects.all()

    def resolve_all_propietarios(self, info, **kwargs):
        return Propietario.objects.all()

class CreateAuto(graphene.Mutation):
    id = graphene.Int()
    marca = graphene.String()
    modelo = graphene.String()
    color = graphene.String()
    matricula = graphene.String()
    ano = graphene.Int()
    imagen_url = graphene.String()
    propietario = graphene.Field(PropietarioType)

    class Arguments:
        marca = graphene.String()
        modelo = graphene.String()
        color = graphene.String()
        matricula = graphene.String()
        ano = graphene.Int()
        imagen_url = graphene.String()
        propietario_id = graphene.Int()

    def mutate(self, info, marca, modelo, color, matricula, ano, imagen_url, propietario_id):
        propietario = Propietario.objects.get(pk=propietario_id)
        auto = Auto(marca=marca, modelo=modelo, color=color, matricula=matricula, ano=ano, imagen_url=imagen_url, propietario=propietario)
        auto.save()
        return CreateAuto(
            id=auto.id,
            marca=auto.marca,
            modelo=auto.modelo,
            color=auto.color,
            matricula=auto.matricula,
            ano=auto.ano,
            imagen_url=auto.imagen_url,
            propietario=auto.propietario
        )

class CreatePropietario(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    apellido = graphene.String()
    fecha_nacimiento = graphene.String()
    email = graphene.String()
    telefono = graphene.String()
    direccion = graphene.String()

    class Arguments:
        nombre = graphene.String()
        apellido = graphene.String()
        fecha_nacimiento = graphene.String()
        email = graphene.String()
        telefono = graphene.String()
        direccion = graphene.String()

    def mutate(self, info, nombre, apellido, fecha_nacimiento, email, telefono, direccion):
        propietario = Propietario(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, email=email, telefono=telefono, direccion=direccion)
        propietario.save()
        return CreatePropietario(
            id=propietario.id,
            nombre=propietario.nombre,
            apellido=propietario.apellido,
            fecha_nacimiento=propietario.fecha_nacimiento,
            email=propietario.email,
            telefono=propietario.telefono,
            direccion=propietario.direccion
        )

class Mutation(graphene.ObjectType):
    create_auto = CreateAuto.Field()
    create_propietario = CreatePropietario.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
