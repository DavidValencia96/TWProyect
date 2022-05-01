from django.shortcuts import redirect, render
from .models import Profile, Post
from .forms import userRegisterForm, PostForm
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.all()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user # asignamos el id del usuario en sesión
            post.save()
            return redirect('home')
    else: 
        form = PostForm()
    
    context = {
        'posts': posts, 
        'form': form,
    }
    return render(request, 'twitter/newsfeed.html', context)

def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = userRegisterForm()
            
    context={'form': form}
    return render(request, 'twitter/register.html', context)

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')


def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {'user': user, 'posts': posts}
    return render(request, 'twitter/profile.hmtl', context)

# https://www.youtube.com/watch?v=06aDhOwqvfY&ab_channel=MundoPython encontrar solución a la linea 45