from django.shortcuts import render

def project(request):
    return render(request, "about.html")
