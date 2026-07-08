from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Category, Comment

# Register your models here.

class PostAdmin(SummernoteModelAdmin): #admin.ModelAdmin
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    
    summernote_fields = ('content',)

class CommitAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date')
    list_filter = ('approved', 'post')
    search_fields = ['title', 'post']

    summernote_fields = ('message',)

admin.site.register(Comment, CommitAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)