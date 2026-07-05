from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag
def function():
    return "hello"

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}