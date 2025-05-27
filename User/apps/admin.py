from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.models import User


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "phone_number", "password1", "password2", "email"),
            },
        ),
    )
