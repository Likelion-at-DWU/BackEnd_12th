from django.shortcuts import render,redirect, get_object_or_404
from .forms import SpringFoodModelForm
from .models import SpringFood
# Create your views here.

def spring(request):
    springposts = SpringFood.objects.all().order_by('-created_at')
   
    return render(request,"spring.html", {"springposts" : springposts})

def createSpringFood(request):
    if request.method == 'POST':
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

    return render(request,"post_detail.html",{"post": post})

# 글 수정

def post_update(request, id):
    post = get_object_or_404(SpringFood,pk=id)
    if request.method == 'POST':
        form = SpringFoodModelForm(request.POST, instance =post)
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
