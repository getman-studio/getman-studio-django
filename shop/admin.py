from django.contrib import admin
from models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"text_id": ("name",)}

admin.site.register(Category, CategoryAdmin)
