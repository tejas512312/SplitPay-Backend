from spay import models


class GroupListResolver:
    """ Resolver used to fetch all groups of particular user """

    def __call__(self, *args, **kwargs):
        try:
            groups = models.Group.objects.filter(users=kwargs.get('id'))
            return groups
        except Exception as e:
            print(e)


class ExpenseListResolver:
    """ Resolver used to fetch all expenses of group """
    def __call__(self, *args, **kwargs):
        try:
            expense = models.Expense.objects.filter(group=kwargs.get('id'))
            return expense
        except Exception as e:
            print(e)
