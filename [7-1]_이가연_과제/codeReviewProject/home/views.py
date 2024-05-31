from django.shortcuts import render, redirect
from .forms import ReviewModelForm

def home(request):
    return render(request, "index.html")

def create(request) : 
    if request.method == 'POST' or request.method == 'FILES' : 
        form = ReviewModelForm(request.POST, request.FILES)
        if form.is_valid() :
            #form.save()
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('home')
    else :
        form = ReviewModelForm()
    return render(request, 'form_create.html', {'form':form})