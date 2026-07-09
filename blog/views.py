from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post, Comment
from blog.forms import CommentsForm
from django.contrib import messages

def index_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get("cat_name") != None:
        posts = posts.filter(category__name=kwargs["cat_name"].lower())

    if kwargs.get("author_username") != None:
        posts = posts.filter(author__username=kwargs["author_username"])

    if kwargs.get("tag_name") != None:
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])
    
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_view(request, pid):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment submitted successfully.')
        else:
            messages.add_message(request, messages.ERROR, "Your comment didn't submitted.")
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid, status=1)
    
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

    comments = Comment.objects.filter(post=post.id, approved=True).order_by('-created_date')

    form = CommentsForm()
    
    context = {
        "post": post,
        "prev_post": prev_post,
        "next_post": next_post,
        "comments" : comments,
        "form" : form,
    }
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'): 
            posts = posts.filter(Q(content__icontains=s) | Q(title__icontains=s))
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def test(request):
    return render(request, 'test.html')
