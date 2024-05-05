from django.shortcuts import render, redirect, get_object_or_404
from travels.models import Post
from travels.forms import PostModelForm

# Create your views here.
def post(request):
    return render(request, "post.html")

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "post_list.html", {"posts" : posts})

def post_detail(request, post_id) : 
    post = Post.objects.get(id=post_id)
    
    return render(request, "post_detail.html", {"post" : post})

def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
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