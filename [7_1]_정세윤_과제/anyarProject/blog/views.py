from django.shortcuts import render, redirect, get_object_or_404
from page.models import Post, Comment
from page.forms import PostModelForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.
def blog(request):
    return render(request, "blog.html")

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

    if filled_form.is_valid():        # 유효성 먼저 검사 !! 
        finished_form = filled_form.save(commit=False) # 먼저 임시 저장 
        finished_form.article = get_object_or_404(Post, pk=id) # 해당 post 가져오고     
        finished_form.author = request.user
        finished_form.save()  # 저장하기 
    return redirect('post_detail', id)

def update_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com) # 원래의 댓글폼을 가져옵니다 
    
    if request.method == "POST": # 수정(POST)을 요청했을 땐 !!
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid(): # 유효하면 
            update_form.save() # 저장하기 
            return redirect('post_detail', post_id) # 다시 상세 페이지로 redirect
    else: # POST 요청이 아닐 때(-> GET 요청 일 때) : 댓글 수정 페이지로 render 
        return render(request, 'comment_update.html', {'comment_form' : comment_form})
    
def delete_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('post_detail', post_id)

def bookmark(request, post_id):
    if request.user.is_authenticated:
        article = Post.objects.get(pk=post_id)
        if article.bookmark_user.filter(pk=request.user.pk).exists():
            # 좋아요 취소 (remove)
            article.bookmark_user.remove(request.user)
        else:
            # 좋아요 추가 (add)
            article.bookmark_user.add(request.user)
        
    return redirect('post_detail', post_id)

def bookmark_list(request):
    bookmarks = Post.objects.filter(bookmark_user=request.user).order_by('-created_at')
    return render(request, "bookmark_list.html", {"bookmarks" : bookmarks})