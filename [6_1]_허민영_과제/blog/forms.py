from django import forms
from .models import Post,Comment
from .widgets import starWidget

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','info','receipe','photo']

        widgets = {
            'info': forms.Textarea(attrs={
                'class': 'custom-textarea',
                'rows': 5,
                'cols': 50,
            }),
            'receipe': forms.Textarea(attrs={
                'class': 'custom-textarea',
                'rows': 10,
                'cols': 50,
            }),
        }
    
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment','grade']

        widgets  ={
            'grade': starWidget,
        }