from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Post
from django.http import Http404

class IndexView(generic.ListView):
    template_name = 'Index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]

class BlogPost(generic.DetailView):
    model = Post
    template_name = 'blog_post.html'


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
def create_post(request):
    if request.method == "POST":
        # Assuming you're sending title, content, etc. from a form
        new_post = Post(title=request.POST['title'], content=request.POST['content'])
        new_post.save()
        return HttpResponseRedirect(reverse('api:blog_post', args=(new_post.id,)))
    else:
        # If it's a GET request, just show the post creation form
        return render(request, 'create_post.html')  # Replace with your template for creating posts




