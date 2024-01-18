from django.shortcuts import render
from .serializers import *
from .models import *
from django.http import JsonResponse
# Create your views here.

def experience(request):
    experience_list = Experience.objects.filter(public=True)
    serializer = ExperienceSerializer(experience_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def projects(request):
    project_list = Project.objects.all()
    serializer = ProjectSerializer(project_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def articles(request):
    article_list = Article.objects.all()
    serializer = ArticleSerializer(article_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def contacts(request):
    contact_list = Contact.objects.all()
    serializer = ContactSerializer(contact_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def index(request):
    return JsonResponse({"message": "Chiso's Resume Data API"})