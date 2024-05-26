from django.shortcuts import redirect, render
from .forms import PostModelForm
from django.contrib.auth.models import User

def home(request):
		return render(request, "index.html")

def create(request):
    if request.method == 'POST' or request.method == 'FILES': 
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid(): 
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('home')
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})

def signup(request):
    if request.method=='POST':
        if request.POST['password'] == request.POST['repeat']:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            print('회원가입 성공')
            return redirect('home')
    return render(request, 'signup.html')