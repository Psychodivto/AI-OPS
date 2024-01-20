import graphene

from graphene_django import DjangoObjectType
from sistema.models import CustomUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username", "password")
        
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    
    def resolve_users(self, info):
        return CustomUser.objects.all()
    
class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    
    class Arguments:
        email = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        
    def mutate(self, info, email, username, password):
        user = CustomUser(email=email, username=username, password=password)
        user.save()
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)