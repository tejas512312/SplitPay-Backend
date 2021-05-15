import graphene


class UserInput(graphene.InputObjectType):
    id = graphene.Int(required=True)


class UserInputPrice(graphene.InputObjectType):
    id = graphene.Int(required=True)
    price = graphene.Int(required=True)


class GroupInput(graphene.InputObjectType):
    """ fields are required to create group """

    name = graphene.String(required=True)
    users = graphene.List(UserInput, required=True)


class GroupIdInput(graphene.InputObjectType):
    id = graphene.Int(required=True)


class ExpenseInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    amount = graphene.Int(required=True)
    group = graphene.Int(required=True)
    friends = graphene.List(UserInput, required=True)
    paidBy = graphene.List(UserInput, required=True)
