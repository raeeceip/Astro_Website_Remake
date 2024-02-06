from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'api'
urlpatterns = [
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('articles/', views.articles, name='articles'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.index, name='index'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

