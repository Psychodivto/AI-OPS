import graphene

from graphene_django import DjangoObjectType
from sistema.models import CustomUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username", "password")
        
class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
    
    def resolve_users(self, info):
        return CustomUser.objects.all()
    
    
class Mutation(graphene.ObjectType):
    create_users = graphene.Field(UserType, email=graphene.String(), username=graphene.String(), password=graphene.String())
    
    def resolve_create_users(self, info, email, username, password):
        user = CustomUser(email=email, username=username, password=password)
        user.set_password(password)
        user.save()
        return user
    
    login = graphene.Field(UserType, username=graphene.String(), password=graphene.String())
    
    def resolve_login(self, info, username, password):
        user = CustomUser.objects.get(username=username)
        if user.check_password(password):
            return user
        raise Exception('Usuario o contraseña incorrectos')
    
    update_user = graphene.Field(UserType, id=graphene.Int(), email=graphene.String(), username=graphene.String(), password=graphene.String())
    
    def resolve_update_user(self, info, id, email, username, password):
        user = CustomUser.objects.get(id=id)
        user.email = email
        user.username = username
        user.set_password(password)
        user.save()
        return user
    
    delete_user = graphene.Field(UserType, id=graphene.Int())
    
    def resolve_delete_user(self, info, id):
        user = CustomUser.objects.get(id=id)
        user.delete()
        return user
       
schema = graphene.Schema(query=Query, mutation=Mutation)