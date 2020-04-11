import graphene
from django.contrib.auth import get_user_model

from users.schema import UserType


class CreateUserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    email = graphene.String(required=True)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = CreateUserInput(required=True)

    def mutate(self, info, input):
        user = get_user_model()(username=input.username, email=input.email)
        user.set_password(input.password)
        user.save()

        return CreateUser(user=user)


class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
