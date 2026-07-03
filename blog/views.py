from django.shortcuts import render
from blog.models import Post

def index_view(request):
    return render(request, 'blog/blog-home.html')

def single_view(request):
    return render(request, 'blog/blog-single.html')

def test(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'test.html', context)
