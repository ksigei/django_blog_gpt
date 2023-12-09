from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    print("posts", posts)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

from .forms import PostForm

@login_required
def post_create(request):

    user = request.user

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # Set the author to the currently logged-in user (assuming you have user authentication)
            post.author = user.author
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})
