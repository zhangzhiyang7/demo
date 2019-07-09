from django.contrib import admin
from .models import BlogType, Blog
# Register your models here.


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")
    ordering = ("id",)


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ("title", "content", "author", "last_updated_time", "blog_type")
    ordering = ("id",)
