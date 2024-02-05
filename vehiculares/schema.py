import graphene
import graphql_jwt
import sistema.schemas.users
import sistema.schemas.sistema
import sistema.schemas.sistema_relay


class Query(sistema.schemas.users.Query,
            sistema.schemas.sistema.Query,
            sistema.schemas.sistema_relay.RelayQuery,
            graphene.ObjectType):
    pass


class Mutation(sistema.schemas.users.Mutation,
               sistema.schemas.sistema.Mutation,
               graphene.ObjectType):
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)