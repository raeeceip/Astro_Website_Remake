from rest_framework import serializers
from .models import *

class ExperienceSARSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceSAR
        fields = ['index', 'statement']

class ExperienceSerializer(serializers.ModelSerializer):
    experience_sars = ExperienceSARSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ['company', 'title', 'start_date', 'end_date', 'designation', 'experience_sars']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'link']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'link', 'description']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['icon', 'data', 'link']