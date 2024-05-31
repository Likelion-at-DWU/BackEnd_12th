from django import forms
from .models import Review, Comment

class ReviewModelForm(forms.ModelForm) : 
    class Meta :
        model = Review
        fields = ['project_name', 'language', 'code', 'photo']

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment']