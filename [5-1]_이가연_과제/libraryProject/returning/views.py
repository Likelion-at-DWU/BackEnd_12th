from django.shortcuts import render

# Create your views here.
def returning(request):
    return render(request, 'about.html')
