from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('posts/', views.blog_posts, name='blog_posts'),
    path('posts/<int:pk>/', views.BlogPost.as_view(), name='blog_post'),
    path('posts/json/', views.blog_posts_json, name='blog_posts_json'),
    path('posts/create/', views.create_post, name='create_post'),
]

