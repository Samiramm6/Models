from django.contrib import admin
from .models import NewsCategory, News



@admin.register(NewsCategory)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id']
    # list_filter = ['created_at']
    list_display = ['id', 'name']
    ordering = ['-id']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['pr_name', 'id']
    list_display = ['pr_name', 'id']
