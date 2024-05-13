from django.shortcuts import render, redirect
from .forms import PostModelForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES)  # 입력 내용 form 변수에 저장
        if form.is_valid(): 
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('home')
    else:                                   #GET 방식일 경우
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})