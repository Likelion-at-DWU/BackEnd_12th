from django.shortcuts import render, redirect, get_object_or_404
from business.models import Post, Comment
from business.forms import PostModelForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.
def product(request):
    return render(request, "products.html")

def product_list(request):
    products = Post.objects.all().order_by('-created_at')
    paginator = Paginator(products, 5)
    pagnum = request.GET.get('page')
    products = paginator.get_page(pagnum)
    return render(request, "product_list.html", {"products" : products})

def product_detail(request, product_id) : 
    product = Post.objects.get(id=product_id)
    comment_form = CommentForm()
    context = {
        'product':product,
        'comment_form' : comment_form
    }
    
    return render(request, "product_detail.html", context)



def product_update(request, id):
    product = get_object_or_404(Post, pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = PostModelForm(instance=product)
        return render(request, 'form_create.html', {'form':form, 'id':id})
    
def product_delete(request, id):
    product = Post.objects.get(pk=id)
    product.delete()
    return redirect('product_list')

def create_comment(request, id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Post, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('product_detail', id)

def update_comment(request, product_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    comment_form = CommentForm(instance=my_com)
    
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=my_com)
        if update_form.is_valid():
            update_form.save()
            return redirect('product_detail', product_id)
    else: 
        return render(request, 'comment_update.html', {'comment_form' : comment_form})
    
def delete_comment(request, product_id, com_id):
    my_com = Comment.objects.get(id=com_id)
    my_com.delete()

    return redirect('product_detail', product_id)


def like_post(request, product_id):
    product = get_object_or_404(Post, id=product_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user in product.likes.all():
                product.likes.remove(request.user)
            else:
                product.likes.add(request.user)
    return redirect('product_detail', product_id=product_id)

