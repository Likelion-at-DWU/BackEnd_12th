from django.shortcuts import render, redirect, get_object_or_404
from travels.models import Post, Comment
from travels.forms import PostModelForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.
def post(request):
    return render(request, "post.html")

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
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

    if filled_form.is_valid():     # 유효성 검사하기 
        finished_form = filled_form.save(commit=False) # 먼저 임시 저장 
        finished_form.article = get_object_or_404(Post, pk=id) # 해당 post 가져오고     
        finished_form.save()  # 저장하기 
    return redirect('post_detail', id)

def update_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com) # 원래의 댓글폼을 가져온다.
    
    if request.method == "POST": # 수정(POST)을 요청했을 경우
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid(): # 업데이트폼이 유효하면 
            update_form.save() # 저장하기 
            return redirect('post_detail', post_id) # 다시 상세 페이지로 redirect
    else: # GET 요청 일 때 : 댓글 수정 페이지로 render 
        return render(request, 'comment_update.html', {'comment_form' : comment_form})
    
def delete_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('post_detail', post_id)

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    
    return render(request, 'post_list.html', {'posts':posts})