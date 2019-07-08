from django.contrib import admin
from .models import Article
# Register your models here.


# admin.site.register(Article, ArticleAdmin)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "content", "create_time", "last_updated_time", "author", "is_deleted")
    ordering = ("id",)


