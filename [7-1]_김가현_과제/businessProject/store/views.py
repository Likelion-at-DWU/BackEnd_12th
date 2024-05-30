from django.shortcuts import render

# Create your views here.
def store(request):
    return render(request, "store.html")

def like_list(request):
    if request.user.is_authenticated:
        like = request.user.liked_posts.all()
    else:
        like = []
    return render(request, 'like_list.html', {'like': like})