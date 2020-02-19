from django.contrib import admin
from .models import Product, Manufacturer, Category
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'manufacturer']
    prepopulated_fields = {'slug':('name',)}
    search_fields =('name',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Category)
class CategoryAmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

