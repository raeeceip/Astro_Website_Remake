from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Post


def blog_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return HttpResponse("You're looking at post %s." % post_id)

def blog_posts(request):
    "RETURN ALL POSTS"
    posts = Post.objects.all()
    return HttpResponse("You're looking at all posts %s." % posts)

" render blog posts as json "
def blog_posts_json(request):
    "RETURN ALL POSTS"
    posts = Post.objects.all()
    data = serializers.serialize('json', posts)
    return HttpResponse(data, content_type='application/json')


def blog_post_json(request, post_id):
    posts = Post.objects.all()
    data = serializers.serialize('json', [posts, ])
    return HttpResponse(data, content_type='application/json')

def index(request):
    'return all posts '
    posts = Post.objects.all()
    return render(request, 'Index.html', {'posts': posts})


