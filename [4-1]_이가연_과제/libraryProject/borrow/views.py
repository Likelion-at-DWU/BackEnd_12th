from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from search.models import Book
from search.forms import BookModelForm

# Create your views here.
def borrow(request) :
    return render(request, "post.html")

# book_list 요청
def book_list(request) : 
    books = Book.objects.all().order_by('created_at')
    return render(request, "book_list.html", {"books" : books})

# book_detail 요청
def book_detail(request, book_id) : 
    book = Book.objects.get(id=book_id)
    return render(request, "book_detail.html", {"book" : book})

# update
def book_update(request, book_id) :
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST' : 
        form = BookModelForm(request.POST, instance=book)
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