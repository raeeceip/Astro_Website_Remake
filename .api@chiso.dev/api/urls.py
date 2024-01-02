from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('posts/', views.blog_posts, name='blog_posts'),
    path('posts/json/', views.blog_posts_json, name='blog_posts_json'),
]

