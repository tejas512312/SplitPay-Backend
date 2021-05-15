import graphene
from spay import models
from spay.graphql import inputs


class createGroup(graphene.Mutation):
    """ Mutation to create new Group """
    class Arguments:
        new_group = graphene.List(inputs.GroupInput)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, new_group):
        ok = True
        userId = []
        for dict in new_group[0].users:
            for key, val in dict.items():
                try:
                    obj = models.User.objects.get(pk=val)
                    userId.append(val)
                except Exception as e:
                    print(e)
                    ok = False
                    return createGroup(ok=ok)

        query_set = models.Group.objects.create(name=new_group[0].name)
        for id in userId:
            obj = models.User.objects.get(pk=id)
            query_set.users.add(obj)

        return createGroup(ok=ok)


class createExpense(graphene.Mutation):
    """ Mutation to create expense of group """
    class Arguments:
        new_expense = graphene.List(inputs.ExpenseInput)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, new_expense):
        ok = True
        try:
            group = models.Group.objects.get(pk=new_expense[0].group)
            groupUsers = group.users.all()
            friends = []
            paidBy = []
            for obj in new_expense[0].friends:
                for key, val in obj.items():
                    user = groupUsers.filter(id=val)
                    if not user:
                        ok = False
                        return createGroup(ok=ok)
                    else:
                        friends.append(val)

            for obj in new_expense[0].paidBy:
                for key, val in obj.items():
                    if not val in friends:
                        ok = False
                        return createGroup(ok=ok)
                    else:
                        paidBy.append(val)

            expense = models.Expense.objects.create(name=new_expense[0].name,
                                                    amount=new_expense[0].amount,
                                                    group=group
                                                    )
            len1 = len(new_expense[0].friends)
            len2 = len(new_expense[0].paidBy)
            if len1>0 and 0 < len2 <= len1:
                amount = expense.amount
                divide = amount/len1
                take = (divide*(len1-len2))/len2

                for id in paidBy:
                    user = models.User.objects.get(pk=id)
                    expense.paidBy.add(user)

                for id in friends:
                    user = models.User.objects.get(pk=id)
                    if id in paidBy:
                        user.totalBalance += take
                    else:
                        user.totalBalance -= divide
                    user.save()
                    expense.friends.add(user)

        except Exception as e:
            ok = False
            print(e)

        return createGroup(ok=ok)


class Mutation(graphene.ObjectType):
    create_group = createGroup.Field()
    create_expense = createExpense.Field()

