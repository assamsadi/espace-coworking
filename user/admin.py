
# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'phone', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']

admin.site.register(User, UserAdmin)
