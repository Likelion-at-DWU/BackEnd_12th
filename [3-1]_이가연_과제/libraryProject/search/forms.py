from django import forms
from .models import Book

class BookModelForm(forms.ModelForm) : 
    class Meta : 
        model = Book
        fields = ['title', 'author', 'contents'] 