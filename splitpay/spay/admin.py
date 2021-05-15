from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Group)
admin.site.register(Users)
admin.site.register(Expense)
