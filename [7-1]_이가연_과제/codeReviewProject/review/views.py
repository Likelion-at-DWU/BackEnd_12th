from django.shortcuts import render, redirect, get_object_or_404
from home.models import Review, Comment
from home.forms import ReviewModelForm, CommentForm
from django.core.paginator import Paginator

def review(request):
    return render(request, "post.html")

# review_list 요청
def review_list(request) : 
    reviews = Review.objects.all().order_by('-created_at')
    paginator = Paginator(reviews, 5)
    pagnum = request.GET.get('page')
    reviews = paginator.get_page(pagnum)
    return render(request, "review_list.html", {"reviews" : reviews})


# review_detail 요청
def review_detail(request, review_id) : 
    review = get_object_or_404(Review, pk=review_id)
    comment_form = CommentForm()
    context={
        'review':review,
        'comment_form' : comment_form
    }
    return render(request, "review_detail.html", context)

# review_update 요청
def review_update(request, review_id) : 
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST' or request.method == 'FILES':
        form = ReviewModelForm(request.POST, request.FILES, instance=review)
        if form.is_valid() : 
            form.save()
            return redirect('review_list')
    else :
        form  = ReviewModelForm(instance=review)
        return render(request, 'form_create.html', {'form':form, 'review_id':review_id})


# review_delete 요청
def review_delete(request, review_id) :
    review = Review.objects.get(pk=review_id)
    review.delete()
    return redirect('review_list')


# create_comment 요청
def create_comment(request, review_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Review, pk=review_id)    
        finished_form.author = request.user
        finished_form.save()  # 저장하기 
    return redirect('review_detail', review_id)


# update_comment 요청
def update_comment(request, review_id, com_id) :
    my_com = Comment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com) 
    
    if request.method == "POST": 
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid(): 
            update_form.save()
            return redirect('review_detail', review_id) 
    else:
        return render(request, 'comment_update.html', {'comment_form' : comment_form})
    

# delete_comment 요청
def delete_comment(request, review_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('review_detail', review_id)