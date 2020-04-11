import graphene

from users.mutations import UserMutation
from users.schema import UserQuery


class Query(UserQuery, graphene.ObjectType):
    pass


class Mutation(UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=UserQuery, mutation=Mutation)
