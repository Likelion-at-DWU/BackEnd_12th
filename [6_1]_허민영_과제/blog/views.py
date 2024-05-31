from django.shortcuts import redirect, render
from .forms import PostModelForm,CommentForm
from django.db.models import Avg
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def home(request):

    #가장 평균이 높은 칵테일 추천해줌
    highest_rated_post = Post.objects.annotate(avg_rating=Avg('comment__grade')).order_by('-avg_rating').first()
    posts = Post.objects.all().order_by('-created_at')
    # paginator = Paginator(posts, 6)
    # pagnum = request.GET.get('page')
    # posts = paginator.get_page(pagnum)
    
    context = {
        'highest_rated_post': highest_rated_post,
        'posts': posts
    }
    return render(request,"index.html",context)

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('home')
    else:
        form = PostModelForm()
    return render(request, 'form_create.html',{'form': form})
