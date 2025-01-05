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



def addform(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Post.objects.create(title=title, description=description)
        return redirect("/post")
    return render(request, 'task/form.html')