from django.contrib import admin
from posApp.models import Branch, Unit, Category, Products, Sales, salesItems

# Register your models here.
admin.site.register(Branch)
admin.site.register(Unit)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(salesItems)
# admin.site.register(Employees)
