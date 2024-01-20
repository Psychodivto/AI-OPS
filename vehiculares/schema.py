import graphene
import sistema.schemas.users


class Query(sistema.schemas.users.Query, 
            graphene.ObjectType):
    pass


class Mutation(sistema.schemas.users.Mutation, 
               graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)