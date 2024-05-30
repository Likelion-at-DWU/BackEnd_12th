from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Post, Comment
from blog.forms import PostModelForm, CommentForm

# Create your views here.

def post(request):
    return render(request, 'post.html')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()
    whole_post = {
        'post' : post,
        'comment_form' : comment_form
    }
    return render(request, 'post_detail.html', whole_post)

def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id)
    else:
        form = PostModelForm(instance=post)
        return render (request, 'form_create.html', {'form' : form, 'id' : id})
    
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('post_list')

def create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.linked_post = get_object_or_404(Post, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('post_detail', id)

def update_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com)
    if request.method == 'POST':
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid():
            update_form.save()
            return redirect('post_detail', post_id)
    else:
        return render(request, 'comment_update.html', {'comment_form' : comment_form})
    
def delete_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()
    return redirect('post_detail', post_id)

def post_list(request):
    all_posts = Post.objects.all().order_by('-created_at')
    my_paginator = Paginator(all_posts, 5)
    current_page = request.GET.get('page')
    all_posts = my_paginator.get_page(current_page)
    return render(request, 'post_list.html', {'posts':all_posts})

def like_post(request, post_id):
    user = request.user
    if user.is_authenticated:
        post = Post.objects.get(id=post_id)
        if post.liked_users.filter(pk=user.id):
            post.liked_users.remove(user)
            print('좋아요 취소')
        else:
            post.liked_users.add(user)
            print('좋아요 누름')
        return redirect('post_detail', post_id)
    else:
        return redirect('accounts:login')
