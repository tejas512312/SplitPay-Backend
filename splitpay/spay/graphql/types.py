from graphene_django import  DjangoObjectType
from spay.models import *


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = "__all__"


class ExpenseType(DjangoObjectType):
    class Meta:
        model = Expense
        fields = "__all__"

