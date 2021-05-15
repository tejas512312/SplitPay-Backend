from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    emailAddress = models.EmailField()
    phoneNumber = models.BigIntegerField()
    totalBalance = models.FloatField()

    def __str__(self):
        return self.name


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    amount = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=None, related_name='group')
    friends = models.ManyToManyField(User, related_name='friends')
    paidBy = models.ManyToManyField(User, related_name='paidBy')

    def __str__(self):
        return self.name

