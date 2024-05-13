from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from search.models import Book, Comment
from search.forms import BookModelForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.
def borrow(request) :
    return render(request, "post.html")

# book_list 요청
def book_list(request) : 
    books = Book.objects.all().order_by('created_at')
    paginator = Paginator(books, 5)
    pagnum = request.GET.get('page')
    books = paginator.get_page(pagnum)
    return render(request, "book_list.html", {"books" : books})

# book_detail 요청
def book_detail(request, book_id) : 
    book = get_object_or_404(Book, pk=book_id)
    comment_form = CommentForm()
    context={
        'book':book,
        'comment_form' : comment_form
    }
    return render(request, 'book_detail.html', context)


# update
def book_update(request, book_id) :
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST' or request.method == 'FILES': 
        form = BookModelForm(request.POST,  request.FILES, instance=book)
        if form.is_valid() : 
            form.save()
            return redirect('book_list')
    else :
        form = BookModelForm(instance=book)
        return render(request, 'form_create.html',  {'form':form, 'id':book_id})
    

# delete
def book_delete(request, id) :
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('book_list')


# 댓글 생성
def create_comment(request, id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():        # 유효성 먼저 검사 !! 
        finished_form = filled_form.save(commit=False) # 먼저 임시 저장 
        finished_form.article = get_object_or_404(Book, pk=id) # 해당 book 가져오고     
        finished_form.creater = request.user
        finished_form.save()  # 저장하기 
    return redirect('book_detail', id)


# 댓글 수정
def update_comment(request, book_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com) # 원래의 댓글폼을 가져옵니다 
    
    if request.method == "POST": # 수정(POST)을 요청했을 땐 !!
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid(): # 유효하면 
            update_form.save() # 저장하기 
            return redirect('book_detail', book_id) # 다시 상세 페이지로 redirect
    else: # POST 요청이 아닐 때(-> GET 요청 일 때) : 댓글 수정 페이지로 render 
        return render(request, 'comment_update.html', {'comment_form' : comment_form})
    


# 댓글 삭제
def delete_comment(request, book_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('book_detail', book_id)