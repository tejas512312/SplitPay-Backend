import graphene
from spay.graphql.query import Query
from spay.graphql.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
