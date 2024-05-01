from django.shortcuts import redirect, render
from .forms import PostModelForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)# 입력 내용을 form이라는 변수에 저장ㅇ
        if form.is_valid(): 
            form.save() #form 데이터를 db에 저장
            return redirect('home')
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})