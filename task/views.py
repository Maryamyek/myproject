from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse

from task.models import Post


# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'task/home.html', context={"home": post})

    # return HttpResponse("hello world")

def list_posts(request):
    posts = Post.objects.all()
    return render(request,'task/task.html', context={"posts":posts})
