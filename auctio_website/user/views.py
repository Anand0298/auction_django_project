from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from buy.models import comments
from django.urls import reverse
from auctio_website.views import pro_page,minimum_bid


# Create your views here.


def register(request):
       if request.method=="POST":
            first_name=request.POST['First name']
            last_name=request.POST['Last name']
            username=request.POST['Username']
            email=request.POST['Email']
            password=request.POST['Password']
            password1=request.POST['Confirm Password']
            if password!=password1:
               return render(request,"register.html",{"message":"password is not matching."})
             
            try:
                 user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                 user.save()
            except IntegrityError:
                 return render(request,"register.html",{"message":"username already taken"})
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
       else:
            return render(request,'register.html')
    

def loginview(request):
    if request.method =="POST":
        username=request.POST['Username']
        password=request.POST['Password']
        user=authenticate(request,username=username, password=password)
        if(user is not None):
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request,"login.html",{"message":"Invalid Credentials"})
    else:
        return render(request, "login.html")
    
def logoutview(request):
    logout(request)
    print("logged out")
    return redirect("home")


@login_required(login_url="register")
def sell(request):
    if request.method=='POST':
        conduct_bid=bidProducts()
        conduct_bid.user=request.user.username
        conduct_bid.desc=request.POST['description']
        conduct_bid.start_price=request.POST['start_price']
        conduct_bid.category=request.POST['category']
        conduct_bid.title=request.POST['pro_name']
        conduct_bid.image=request.POST['img_url']
        conduct_bid=bidProducts(username=conduct_bid.user,desc=conduct_bid.desc,start_price=conduct_bid.start_price,category=conduct_bid.category,title=conduct_bid.title,image=conduct_bid.image)
        conduct_bid.save()
        return redirect("home")
    return render(request,"sell.html")

@login_required(login_url="register")
def all_comments(request):

    comment=request.GET['comment']
    id=request.GET['listid']
    user=request.user.username
    newcomment=comments(user=user, comment=comment, pro_id=id)
    newcomment.save()
    return pro_page(request,id)
        
