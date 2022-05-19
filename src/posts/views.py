from django.shortcuts import redirect, render,get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.urls import is_valid_path
from .models import Post, Comment

def home(request):
    return render(request, 'home.html')


def posts(request):
    posts = Post.objects.all().order_by("-created_date", "-id")   # SELECT * FROM posts

    print(posts)
    # return HttpResponse("Publicaciones")

    return render(request, 'posts/posts.html', {
        'posts': posts
    })


def post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=id)

    return render(request, 'posts/post.html', {'post':post, 'comments': comments})


def create_post(request):
    if request.method == "POST":
        post = Post(
            title=request.POST['title'],
            description=request.POST['description'],
            img=request.POST['image'],
            content=request.POST['content'],
            author_id=request.user.pk
        )

        post.save()

        return redirect("/posts")

    return render(request, 'posts/create.html')


def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":

        post.title = request.POST['title']
        post.description = request.POST['description']
        post.img = request.POST['image']
        post.content = request.POST['content']


        post.save()

        return redirect("/posts")

    return render(request, 'posts/edit.html', {'post': post})


def delete_post(request,id):
    post = Post.objects.get(id=id)

    post.delete()
    return redirect("/posts")
    
 
def create_comment(request, id):
    post = get_object_or_404(Post,pk=id)
    comments = post.comments.filter(activate=True)
    new_comment = None

    if request.method == 'POST':
        body = request.POST['com_content']
        username = request.user.username
        if body:
            new_comment = Comment.objects.create(
                author = username,
                body = body,
            )
            new_comment.post = post
            new_comment.save()
            return redirect("/posts")
    
    return render(request, 'posts/posts.html', {
        'post':post,
        'comments':comments,
        'new_comment':new_comment,
    })

