from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from questioning_app.models import User, Product, Order


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
