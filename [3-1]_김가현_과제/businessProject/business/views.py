from django.shortcuts import redirect, render
from .forms import PostModelForm

def home(request):
    return render(request,"index.html")

def create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('home')
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})