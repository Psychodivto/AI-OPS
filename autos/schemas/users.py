import graphene

from graphene_django.types import DjangoObjectType

from autos.models import CustomUser

class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "fecha_nacimiento", "direccion")


class Query(graphene.ObjectType):
    get_user = graphene.Field(CustomUserType, id=graphene.Int())
    get_all_users = graphene.List(CustomUserType)

    def resolve_get_user(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return CustomUser.objects.get(pk=id)

        return None
    
    def resolve_get_all_users(self, info, **kwargs):
        return CustomUser.objects.all()
        
class CreateUser(graphene.Mutation):
    id = graphene.Int()
    username = graphene.String()
    fecha_nacimiento = graphene.Date()
    direccion = graphene.String()

    class Arguments:
        username = graphene.String()
        fecha_nacimiento = graphene.Date()
        direccion = graphene.String()

    def mutate(self, info, username, fecha_nacimiento, direccion):
        user = AbstractUser(username=username, fecha_nacimiento=fecha_nacimiento, direccion=direccion)
        user.save()

        return CreateUser(
            id=user.id,
            username=user.username,
            fecha_nacimiento=user.fecha_nacimiento,
            direccion=user.direccion,
        )
    
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)