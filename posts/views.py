from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, PictureForm
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # if the form is valid
        if form.is_valid():
            #YES, Save
            form.save()
            #Redirect to home
            return HttpResponseRedirect('/')

        else:
            #No, Show Error
            return HttpResponseRedirect(form.errors.as_json())



    #get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')

    #Show
    return render(request, 'posts.html', 
                {'posts': posts})

def delete(request, post_id):
    #Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    # Find post
    posts = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else: 
            return HttpResponseRedirect(form.errors.as_json())


    # form = PostForm

    # show
    return render(request, 'edit.html', {'posts': posts})

def like(request, post_id):
    newlike = Post.objects.get(id=post_id)
    newlike.likes += 1
    newlike.save()
    return HttpResponseRedirect('/')    
    
      