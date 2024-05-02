from django.shortcuts import render,redirect
from .forms import SpringFoodModelForm

# Create your views here.

def spring(request):
    return render(request,"spring.html")

def createSpringFood(request):
    if request.method == 'POST':
        form = SpringFoodModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('spring')
    else:
        form = SpringFoodModelForm()
    return render(request, 'Springform_create.html',{'form':form})