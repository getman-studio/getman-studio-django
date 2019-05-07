from django.contrib import admin
from .models import Category, GalleryItem, Article, WorkshopParallaxItem

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"text_id": ("name",)}


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"text_id": ("name",)}


class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(GalleryItem, GalleryItemAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(WorkshopParallaxItem)
