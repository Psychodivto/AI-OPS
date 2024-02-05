import graphene

from graphene_file_upload.scalars import Upload
from graphql import GraphQLError
from graphene_django import DjangoObjectType
from sistema.models import Auto, Propietario

class AutoType(DjangoObjectType):
    class Meta:
        model = Auto
        fields = ("id", "marca", "modelo", "anio", "matricula", "color", "adquisicion", "imagen")
        
class PropietarioType(DjangoObjectType):
    class Meta:
        model = Propietario
        fields = ("id", "nombre", "apellido", "dni", "direccion", "telefono", "email", "auto")
        
## Query for get all autos and propietarios, and get autos and propietarios by marca and dni
        
class Query(graphene.ObjectType):
    all_autos = graphene.List(AutoType)
    marca_auto = graphene.List(AutoType, marca=graphene.String())
    all_propietarios = graphene.List(PropietarioType)
    dni_propietario = graphene.List(PropietarioType, dni=graphene.Int())
    
    auto = graphene.Field(AutoType, id=graphene.Int())
    propietario = graphene.Field(PropietarioType, id=graphene.Int())
    
    def resolve_all_autos(root, info):
        return Auto.objects.all()
    
    def resolve_all_propietarios(root, info):
        return Propietario.objects.all()
    
    def resolve_marca_auto(root, info, marca):
        return Auto.objects.filter(marca=marca)
    
    def resolve_dni_propietario(root, info, dni):
        return Propietario.objects.filter(dni=dni)
    
    def resolve_auto(root, info, id):
        try:
            return Auto.objects.get(pk=id)
        except Auto.DoesNotExist:
            return None
        
    def resolve_propietario(root, info, id):
        try:
            return Propietario.objects.get(pk=id)
        except Propietario.DoesNotExist:
            return None
        
## Mutation for create a new Auto and Propietario
    
class CreateAuto(graphene.Mutation):
    id = graphene.Int()
    auto = graphene.Field(AutoType)
    
    class Arguments:    
        marca = graphene.String()
        modelo = graphene.String()
        anio = graphene.Int()
        matricula = graphene.String()
        color = graphene.String()
        adquisicion = graphene.Date()
        imagen = Upload(required=True)
        
        
    def mutate(self, info, marca, modelo, anio, matricula, color, adquisicion, imagen, **kwargs):
        auto = Auto(marca=marca, modelo=modelo, anio=anio, matricula=matricula, color=color, adquisicion=adquisicion, imagen=imagen)
        auto.save()
        
        return CreateAuto(auto=auto)
                
class CreatePropietario(graphene.Mutation):
    id = graphene.Int()
    propietario = graphene.Field(PropietarioType)
    
    class Arguments:
        nombre = graphene.String()
        apellido = graphene.String()
        dni = graphene.Int()
        direccion = graphene.String()
        telefono = graphene.String()
        email = graphene.String()
        auto_id = graphene.Int()
        
    def mutate(self, info, nombre, apellido, dni, direccion, telefono, email, auto_id):
        auto = Auto.objects.get(pk=auto_id)
        propietario = Propietario(nombre=nombre, apellido=apellido, dni=dni, direccion=direccion, telefono=telefono, email=email, auto=auto)
        propietario.save()
        
        return CreatePropietario(id=propietario.id)
        
class Mutation(graphene.ObjectType):
    create_auto = CreateAuto.Field()
    create_propietario = CreatePropietario.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)