from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout  
from django.views.generic import UpdateView
from .models import Post
from . import models
from django.urls import reverse_lazy


def loginn(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(username=name , password=password)
        if user:
            login(request,user)
            return redirect("/home")
        else:
            return redirect("/")
    return render(request , "login.html")

def signup(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newuser = User.objects.create_user(username=name , email=email , password=password)
        newuser.save()
        return redirect("/")
    return render(request , "signup.html")

def home(request):
    postdata = Post.objects.all()
    return render(request,"home.html" , {'postdata':postdata})


def newpost(request):
    if request.method=="POST":
        # author = request.POST.get('author')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        # en = Post(author=request.user , title=title , desc=desc , date=date)
        en = models.Post(title=title , desc = desc , date = date , author = request.user)
        en.save()
        return redirect("/home")
    return render(request , "newpost.html")


def mypost(request):
    posts = Post.objects.filter(author = request.user)
    return render(request , "mypost.html" , {'posts':posts})

def signout(request):
    logout(request)
    return redirect('/')

class studentupdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('mypost')



