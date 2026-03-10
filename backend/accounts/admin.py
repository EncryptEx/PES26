from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("App fields", {"fields": ("tipus",)}),
    )
    list_display = ("id", "username", "email", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")