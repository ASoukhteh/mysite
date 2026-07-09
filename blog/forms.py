from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField

class CommentsForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = ['post' ,'name', 'subject', 'email', 'message']

