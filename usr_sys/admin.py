from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'real_name', 'stu_code', 'nickname', 'email_validated',
        'is_admin'
    ]
    search_fields = ['username', 'real_name', 'stu_code', 'nickname']


from main.helpers import auto_admin
auto_admin(models)