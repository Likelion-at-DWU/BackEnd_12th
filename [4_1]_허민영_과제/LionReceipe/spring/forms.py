from django import forms
from .models import SpringFood

class SpringFoodModelForm(forms.ModelForm):
    class Meta:
        model = SpringFood
        fields = ['title','body','image']