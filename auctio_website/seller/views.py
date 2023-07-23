from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from buy.models import bidding
from django.contrib import messages
from user.models import bidProducts
from .models import *
from auctio_website.views import minimum_bid,pro_page


def categories(request, cat_name):
    category=bidProducts.objects.filter(category=cat_name)
    return render(request,"home.html",{
        "prod":category,
        "cats":bidProducts.objects.values('category').distinct,
    })

# the above function shows the products that are paticularly there in that category list

def category_list(request):

    cat_prod=bidProducts.objects.values('category').distinct
    return render(request,"category.html",{
        "cat_list":cat_prod
    })

@login_required(login_url='register')
def bid(request):
    bid_amount=request.GET['bid_amnt']
    list_id=request.GET['list_d']
    bid_present=bidding.objects.filter(pro_id=list_id)
    startingbid=bidProducts.objects.get(pk=list_id)
    min_bid=startingbid.start_price
    min_bid=minimum_bid(min_bid,bid_present)

    if int(bid_amount)>int(min_bid):

            mybid=bidding(user=request.user.username,pro_id=list_id,bid=bid_amount)
            mybid.save()
            messages.success(request,"Bid Placed")
            return redirect("home")
    
    
    return pro_page(request,list_id)




    





    



    

        