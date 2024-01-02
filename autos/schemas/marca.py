import graphene

from graphene_django.types import DjangoObjectType

from autos.models import Marca


class MarcaType(DjangoObjectType):
    
        class Meta:
            model = Marca
            fields = ("id", "nombre")
            
class Query(graphene.ObjectType):
    all_marcas = graphene.List(MarcaType)
    marca = graphene.Field(MarcaType, id=graphene.Int())
    
    def resolve_all_marcas(self, info, **kwargs):
        return Marca.objects.all()
    
    def resolve_marca(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Marca.objects.get(pk=id)
        return None
    
schema = graphene.Schema(query=Query)