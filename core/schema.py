import graphene

import autos.schemas.autos
import autos.schemas.propietarios


class Query(autos.schemas.autos.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)


class Mutation(autos.schemas.autos.Mutation,
               graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)