from django.shortcuts import redirect, render
from .forms import PostModelForm # froms에서 PostModelForm을 가지고 온다.

# Create your views here.
def page(request):
    return render(request, "index.html")

def create(request):
    if request.method == 'POST': # POST 방식으로 요청이 들어왔을 때
        form = PostModelForm(request.POST) # 입력 내용을 form이라는 변수에 저장ㅇ
        if form.is_valid(): # 만약 form이 유효하다면(= models.py에서 정의한 필드에 적합하다면)
            form.save() #form 데이터를 db에 저장
            return redirect('page') # page으로 redirect
    else: # POST 방식이 아닌 GET 방식으로 요청이 들어왔을 때
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})