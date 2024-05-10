from django.shortcuts import render,redirect, get_object_or_404
from .forms import SpringFoodModelForm, CommentForm
from .models import SpringFood, Comment
from django.core.paginator import Paginator

# Create your views here.

def spring(request):
    springposts = SpringFood.objects.all().order_by('-created_at')
    paginator = Paginator(springposts, 5)
    pagnum = request.GET.get('page')
    springposts = paginator.get_page(pagnum)
    return render(request, 'spring.html', {'springposts':springposts})

def createSpringFood(request):
    if request.method == 'POST' or request.method == 'FILES': 
        form = SpringFoodModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('spring')
    else:
        form = SpringFoodModelForm()
    return render(request, 'Springform_create.html',{'form':form})

#글 조회

def post_detail(request, post_id):
    post = SpringFood.objects.get(id=post_id)
    comment_form = CommentForm()
    context={
        'post':post,
        'comment_form' : comment_form
    }
    return render(request, 'post_detail.html', context)

# 글 수정

def post_update(request, id):
    post = get_object_or_404(SpringFood,pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = SpringFoodModelForm(request.POST, request.FILES, instance =post)
        if form.is_valid():
            form.save()
            return redirect('spring')
    else:
        form = SpringFoodModelForm(instance=post)
        return render(request, 'Springform_create.html',{'form':form, 'id': id})

# 글 삭제

def post_delete(request, id):
    post = SpringFood.objects.get(pk=id)
    post.delete()
    return redirect('spring')

# 댓글 작성
def create_comment(request, id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():        # 유효성 먼저 검사 !! 
        finished_form = filled_form.save(commit=False) # 먼저 임시 저장 
        finished_form.article = get_object_or_404(SpringFood, pk=id) # 해당 post 가져오고     
        finished_form.save()  # 저장하기 
    return redirect('post_detail', id)


# 댓글 수정
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
    

# 댓글 삭제
def delete_comment(request, post_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('post_detail', post_id)

    