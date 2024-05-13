from django import forms
from .models import SpringFood,Comment

class SpringFoodModelForm(forms.ModelForm):
    class Meta:
        model = SpringFood
        fields = ['title','body','image']

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment 
        fields = ['comment']