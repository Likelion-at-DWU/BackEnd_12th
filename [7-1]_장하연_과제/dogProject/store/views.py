from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def store(request):
    return render(request, "store.html")