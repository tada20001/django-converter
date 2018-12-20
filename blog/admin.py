from django.contrib import admin
from .models import Post, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category']  # select2 위젯으로 동작
