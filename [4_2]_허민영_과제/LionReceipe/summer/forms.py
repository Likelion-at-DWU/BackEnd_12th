from django import forms
from .models import SummerFood

class SummerFoodModelForm(forms.ModelForm):
    class Meta:
        model = SummerFood
        fields = ['title','body','image']