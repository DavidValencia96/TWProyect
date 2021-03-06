import http.client
import base64 as b64
import json
from datetime import datetime

from django.shortcuts import redirect, render
from .models import Post, Relationship
from .forms import UserRegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# el login es requerido para ejecutar algunas funciones
# @login_required
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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
            
    context={
        'form': form
    }
    return render(request, 'twitter/register.html', context)

@login_required
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')

# def poster(request, post_id):
#     user = User.objects.get(id=post_id)
#     posts = User.post.id
#     context = {
#         'user': user, 
#         'posts': posts
#     }
#     return redirect(request, 'twitter/poster.html', context)

def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.post.all()
    context = {
        'user': user, 
        'posts': posts
    }
    return render(request, 'twitter/profile.html', context)


@login_required
def editar(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm()
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'twitter/editar.html', context)


@login_required
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'sigues a {username}')
    return redirect('home')


@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.get(from_user=current_user.id, to_user=to_user_id)
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('home')
    
    
    
    