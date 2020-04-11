import graphene

from users.mutations import UserMutation


# class Query(graphene.ObjectType):
#     pass


class Mutation(UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutation)
