from django.shortcuts import render, redirect, get_object_or_404
from business.models import Post
from business.forms import PostModelForm

# Create your views here.
def product(request):
    return render(request, "products.html")

def product_list(request):
    products = Post.objects.all().order_by('-created_at')
    return render(request, "product_list.html", {"products" : products})

def product_detail(request, product_id) : 
    product = Post.objects.get(id=product_id)
    
    return render(request, "product_detail.html", {"product" : product})

def product_update(request, id):
    product = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=product)
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