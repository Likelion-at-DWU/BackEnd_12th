from django.shortcuts import render, redirect,  get_object_or_404
from blog.models import Post, Comment
from blog.forms import PostModelForm, CommentForm
from django.core.paginator import Paginator

def about(request):
		return render(request, "about.html")

def about_list(request):
    about = Post.objects.all().order_by('-created_at')
    paginator = Paginator(about, 5)
    pagnum = request.GET.get('page')
    about = paginator.get_page(pagnum)
    return render(request, "about_list.html", {"about" : about})

def about_detail(request, post_id) : 
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    context={
        'post':post,
        'comment_form' : comment_form
    }
    return render(request, "about_detail.html", context)

def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST'or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('about_list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create.html', {'form':form, 'id':id})
    
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('about_list')

def create_comment(request, id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():        # 유효성 먼저 검사 !! 
        finished_form = filled_form.save(commit=False) # 먼저 임시 저장 
        finished_form.article = get_object_or_404(Post, pk=id) # 해당 post 가져오고 
        finished_form.author = request.user    
        finished_form.save()  # 저장하기 
    return redirect('about_detail', id)

def update_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com) # 원래의 댓글폼을 가져옵니다 
    
    if request.method == "POST": # 수정(POST)을 요청했을 땐 !!
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid(): # 유효하면 
            update_form.save() # 저장하기 
            return redirect('about_detail', post_id) # 다시 상세 페이지로 redirect
    else: # POST 요청이 아닐 때(-> GET 요청 일 때) : 댓글 수정 페이지로 render 
        return render(request, 'comment_update.html', {'comment_form' : comment_form})
    
def delete_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('about_detail', post_id)