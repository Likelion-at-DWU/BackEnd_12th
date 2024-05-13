from django.shortcuts import redirect, render
from .forms import PostModelForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES) # 입력 내용을 form이라는 변수에 저장
        if form.is_valid(): 
            # form.save() #form 데이터를 db에 저장
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('home')
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})