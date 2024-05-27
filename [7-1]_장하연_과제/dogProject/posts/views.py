from django.shortcuts import render, redirect, get_object_or_404
from dog.models import Post, Comment
from dog.forms import PostModelForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.

def post(request):
    return render(request, "products.html")

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    return render(request, "post_list.html", {"posts" : posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    context={
        'post':post,
        'comment_form' : comment_form
    }
    return render(request, 'post_detail.html', context)

def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create.html', {'form':form, 'id':id})
    
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('post_list')

def create_comment(request, id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():     
        finished_form = filled_form.save(commit=False) 
        finished_form.article = get_object_or_404(Post, pk=id) 
        finished_form.author = request.user
        finished_form.save()  
    return redirect('post_detail', id)

def update_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com) 

    if request.method == "POST": 
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