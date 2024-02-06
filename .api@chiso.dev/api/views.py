from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *
from .models import *



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def experience(request):
    experience_list = Experience.objects.filter(public=True)
    serializer = ExperienceSerializer(experience_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def projects(request):
    project_list = Project.objects.all()
    queryset = Project.objects.all()
    serializer = ProjectSerializer(project_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def articles(request):
    article_list = Article.objects.all()
    serializer = ArticleSerializer(article_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def contacts(request):
    contact_list = Contact.objects.all()
    serializer = ContactSerializer(contact_list, many=True)
    return Response(serializer.data)

def index(request):
    return render(request, 'index.html')
