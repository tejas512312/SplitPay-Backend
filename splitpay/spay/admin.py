from django.contrib import admin
from .models import User, Group, Expense

# Register your models here.

admin.site.register({User,Group,Expense})
