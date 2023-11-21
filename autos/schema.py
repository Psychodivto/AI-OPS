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
    
schema = graphene.Schema(query=Query)
class CreateAuto(graphene.Mutation):
    id = graphene.Int()
    marca = graphene.String()
    modelo = graphene.String()
    color = graphene.String()
    matricula = graphene.Int()
    ano = graphene.Int()
    imagen_url = graphene.String()

    class Arguments:
        marca = graphene.String(required=True)
        modelo = graphene.String(required=True)
        color = graphene.String(required=True)
        matricula = graphene.Int()
        ano = graphene.Int()
        imagen_url = graphene.String(required=True)

    ok = graphene.Boolean()
    autos = graphene.Field(AutoType)

    def mutate(self, info, marca, modelo, color, matricula, ano, imagen_url):
        auto= get_auto_model()(
            marca=marca,
            modelo=modelo,
            color=color,
            matricula=matricula,
            ano=ano,
            imagen_url=imagen_url,
        )

        auto.save()
        ok = True

        return CreateAuto(
            id=auto.id,
            marca=auto.marca,
            modelo=auto.modelo,
            color=auto.color,
            matricula=auto.matricula,
            ano=auto.ano,
            imagen_url=auto.imagen_url,
        )

class Mutation(graphene.ObjectType):
    create_auto = CreateAuto.Field()


