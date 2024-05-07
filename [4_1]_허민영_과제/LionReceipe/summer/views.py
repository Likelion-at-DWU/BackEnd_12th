from django.shortcuts import render,redirect

from summer.forms import SummerFoodModelForm


# Create your views here.
def summer(request):
    return render(request,"summer.html")

def createSummerFood(request):
    if request.method == 'POST':
        form = SummerFoodModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('spring')
    else:
        form = SummerFoodModelForm()
    return render(request, 'Summerform_create.html',{'form':form})