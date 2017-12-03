from django.contrib import admin
from .models import Category, Item

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"text_id": ("name",)}

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
