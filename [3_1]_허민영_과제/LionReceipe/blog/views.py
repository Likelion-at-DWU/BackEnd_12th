from django.shortcuts import redirect, render
from .forms import PostModelForm #forms에서 PostModelForm을 가지고 옵니다. 

# 유저의 요청 request가 들어오면 "파일이름.html"을 띄우게 작성
def home(request):
    return render(request, "index.html")


def create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST) #입력 내용을 form이라는 변수에 저장ㅇ
        if form.is_valid(): 
            form.save() #form 데이터를 db에 저장
            return redirect('home')
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})