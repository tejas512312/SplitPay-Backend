import graphene
from graphene import ObjectType
from graphene.types.generic import GenericScalar
from spay.graphql import types, resolvers


class Query(ObjectType):
    get_groups = graphene.List(types.GroupType, id=graphene.Int(), resolver=resolvers.GroupListResolver())
    get_expenses = graphene.List(types.ExpenseType, id=graphene.Int(), resolver=resolvers.ExpenseListResolver())

