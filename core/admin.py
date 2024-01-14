from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category
from django.contrib.auth.models import Group, User



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock', 'available', 'category', 'image_preview')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=50,
                height=50
            ))
        else:
            return "No image uploaded"

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)



