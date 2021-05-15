from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.fields import BooleanField
import graphene
from graphene.types.scalars import ID
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


class PaidByInput(graphene.InputObjectType):
    id = graphene.ID()


class FriendsInput(graphene.InputObjectType):
    id = graphene.ID()


class AddExpense(graphene.Mutation):
    class Arguments:
        expense_name = graphene.String(required=True)
        total_amount = graphene.Float(required=True)
        paid_by = graphene.List(PaidByInput, required=True)
        friends = graphene.List(FriendsInput, required=True)
        group = graphene.ID(required=True)

    status = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        print(kwargs)
        temp = kwargs.get("paid_by")
        temp1 = kwargs.get("friends")

        group = Group.objects.get(id=kwargs.get("group"))
        e = Expense.objects.create(
            name=kwargs.get("expense_name"),
            totalAmount=kwargs.get("total_amount"),
            group=group,
        )

        for i in temp:
            id_i = i["id"]
            e.paidBy.add(Users.objects.get(id=id_i))

        for i in temp1:
            id_i = i["id"]
            e.friends.add(Users.objects.get(id=id_i))

        return AddExpense(status=True)


class Mutation(graphene.ObjectType):
    update_expense = ExpenseMutation.Field()
    add_expense = AddExpense.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
