from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('', index_view, name = 'index'),
    path('<int:pid>/', single_view, name='single'),
    path('category/<str:cat_name>/', index_view, name='category'),
    path('author/<str:author_username>/', index_view, name='author'),
    path('tag/<str:tag_name>/', index_view, name='tag'),
    path('search/', blog_search, name='search'),
    path('rss/feed/', LatestEntriesFeed()),
    path('test', test, name='test')
]