from django.contrib import admin
from core.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','image','price','stock','available','created_at']
    
admin.site.register(Product, ProductAdmin)
