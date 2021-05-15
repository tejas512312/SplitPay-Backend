from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(models.Model):
    authentic_user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    totalBalance = models.DecimalField(max_digits=100, decimal_places=2)
    photoUrl = models.URLField(null=True)
    phoneNumber = models.BigIntegerField()


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    users = models.ManyToManyField(Users)


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    totalAmount = models.DecimalField(max_digits=100, decimal_places=2)
    paidBy = models.ManyToManyField(Users, related_name="paid_by")
    friends = models.ManyToManyField(Users, related_name="friends")
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="group", default=None
    )
