from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse, JsonResponse

def index_view(request):
    posts = Post.objects.filter(status=1)
    posts = posts.order_by('published_date')
    context = {"posts": posts}
    return render(request, 'website/index.html', context)

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')
