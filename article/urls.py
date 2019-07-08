from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # localhost:8000/article/
    path('<int:article_id>', views.article_detail, name="article_detail"),
    path('', views.article_list, name='article_list'),
]
