from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from blog.models import Post, Comment

# Create your views here.

def mypage(request):
    user_id = request.user.id

    posts = Post.objects.filter(author_id=user_id).order_by('-created_at')
    post_paginator = Paginator(posts, 3)
    current_post = request.GET.get('page')
    posts = post_paginator.get_page(current_post)

    comments = Comment.objects.filter(author_id=user_id).order_by('-date')
    com_paginator = Paginator(comments, 3)
    current_com = request.GET.get('page')
    comments = com_paginator.get_page(current_com)

    liked_posts = request.user.liked_posts.all()
    like_paginator = Paginator(liked_posts, 3)
    current_post = request.GET.get('page')
    liked_posts = like_paginator.get_page(current_post)

    mypage_context = {
        'posts' : posts,
        'comments' : comments,
        'liked_posts' : liked_posts
    }
    return render(request, 'mypage.html', mypage_context)

def myposts(request):
    user_id = request.user.id
    posts = Post.objects.filter(author_id=user_id).order_by('-created_at')
    post_paginator = Paginator(posts, 6)
    current_post = request.GET.get('page')
    posts = post_paginator.get_page(current_post)
    return render(request, 'myposts.html', {'posts':posts})

def mycomments(request):
    user_id = request.user.id
    comments = Comment.objects.filter(author_id=user_id).order_by('-date')
    com_paginator = Paginator(comments, 10)
    current_com = request.GET.get('page')
    comments = com_paginator.get_page(current_com)
    return render(request, 'mycomments.html', {'comments':comments})

def mylikes(request):
    user = request.user
    liked_posts = user.liked_posts.all()
    pag = Paginator(liked_posts, 6)
    current_post = request.GET.get('page')
    liked_posts = pag.get_page(current_post)
    return render(request, 'mylikes.html', {'posts':liked_posts})

def unlike_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.liked_users.remove(request.user)
    return redirect('mylikes')