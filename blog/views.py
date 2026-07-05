from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    
    # Increment view count
    post.counted_views += 1
    post.save()
    
    # Get previous post (older)
    prev_post = Post.objects.filter(
        status=1,
        published_date__lt=post.published_date  # Less than current date
    ).order_by('-published_date').first()  # Newest first, get first = immediate previous
    
    # Get next post (newer)
    next_post = Post.objects.filter(
        status=1,
        published_date__gt=post.published_date  # Greater than current date
    ).order_by('published_date').first()  # Oldest first, get first = immediate next
    
    context = {
        "post": post,
        "prev_post": prev_post,
        "next_post": next_post,
    }
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request, 'test.html')
