from django.db.models import ExpressionWrapper
from django.shortcuts import render
from business.models import Post
from django.db.models import Count

# Create your views here.
# def about(request):
#     return render(request, "about.html")

def ranking_list(request):
    posts = list(Post.objects.all())
    sorted_posts = sorted(posts, key=lambda post: (post.like_count, post.created_at), reverse=True)[:5]
    return render(request, "ranking_list.html", {"rank": sorted_posts})