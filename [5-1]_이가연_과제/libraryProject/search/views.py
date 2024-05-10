from django.shortcuts import render, redirect
from .forms import BookModelForm
# Create your views here.
def search(request):
		return render(request, "index.html")

def create(request) : 
	if request.method == 'POST' or request.method == 'FILES' : 
		form = BookModelForm(request.POST, request.FILES) #입력내용을 form이라는 변수에 저장
		if form.is_valid() :
			form.save() #form 데이터를 db에 저장
			return redirect('search')
	else : 
		form = BookModelForm()
	return render(request, 'form_create.html', {'form':form})