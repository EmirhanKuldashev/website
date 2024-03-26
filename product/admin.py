from django.contrib import admin

from product.models import Product, Category, Review

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Review)
class PostAdmin(admin.ModelAdmin):
    pass
