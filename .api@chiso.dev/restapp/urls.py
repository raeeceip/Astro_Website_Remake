from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import UserViewSet, UserSerializer
# Additionally, we include login URLs for the browsable API.
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('post_test/', views.post_test, name='blog_posts'),
]