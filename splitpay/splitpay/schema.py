from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.fields import BooleanField
import graphene
from graphene_django import DjangoObjectType
from spay.models import Users, Group, Expense


class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        fields = ("id", "name", "email")


class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = ("id", "name", "users")


class ExpenseType(DjangoObjectType):
    class Meta:
        model = Expense


class Query(graphene.ObjectType):
    all_users = graphene.List(UsersType)
    user_involved_groups = graphene.List(GroupType, id=graphene.ID())

    def resolve_all_users(root, info):
        print(info.context.user.is_authenticated, info.context.user)
        return Users.objects.all()

    def resolve_user_involved_groups(root, info, **kwargs):
        return Group.objects.filter(users=kwargs.get("id"))


class ExpenseMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        text = graphene.String(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    status = graphene.Boolean()
    updated_list = graphene.List(ExpenseType)

    @classmethod
    def mutate(cls, root, info, text, id):
        print("Ran")
        # Notice we return an instance of this mutation
        return ExpenseMutation(status=True, updated_list=Expense.objects.all())


class Mutation(graphene.ObjectType):
    update_expense = ExpenseMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
