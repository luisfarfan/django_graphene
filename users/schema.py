import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        info
        return get_user_model().objects.all()
