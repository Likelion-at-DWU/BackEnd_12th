from django.shortcuts import render

# Create your views here.
def categories(request):
    return render(request, "categories.html")
