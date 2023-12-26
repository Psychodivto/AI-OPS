import graphene

import autos.schemas.autos
import autos.schemas.propietarios
import autos.schemas.users


class Query(autos.schemas.autos.Query,
            autos.schemas.propietarios.Query,
            autos.schemas.users.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)


class Mutation(autos.schemas.autos.Mutation,
                autos.schemas.propietarios.Mutation,
               graphene.ObjectType):

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)