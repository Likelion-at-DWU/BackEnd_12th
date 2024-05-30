from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Post
from .forms import PostModelForm

# Create your views here.

def home(request):
    all_posts = Post.objects.all().order_by('-created_at')
    my_paginator = Paginator(all_posts, 2)
    current_page = request.GET.get('page')
    all_posts = my_paginator.get_page(current_page)
    return render(request, 'index.html', {'posts':all_posts})

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            filled_form = form.save(commit=False)
            filled_form.author = request.user
            filled_form.save()
            return redirect('post_list')
    else:
        form = PostModelForm()
    return render(request, 'form_create.html', {'form':form})
