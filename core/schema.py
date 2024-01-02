import graphene

import autos.schemas.autos
import autos.schemas.propietarios
import autos.schemas.marca

class Query(autos.schemas.autos.Query,
            autos.schemas.propietarios.Query,
            autos.schemas.marca.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)


class Mutation(autos.schemas.autos.Mutation,
                autos.schemas.propietarios.Mutation,
               graphene.ObjectType):

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)