from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from user.models import bidProducts
from buy.models import bidding,comments

def home(request):
        return render(request,"home.html",{
              "prod":bidProducts.objects.all(),
              "cats":bidProducts.objects.values('category').distinct,
        })



def pro_page(request,bidid):
    bid_desc=bidProducts.objects.get(pk=bidid,bid_active=True)
    bid_present=bidding.objects.filter(pro_id=bidid)

    return render(request,"products.html",{
        "list":bid_desc,
        "comments":comments.objects.filter(pro_id=bidid),
        "present_bid":minimum_bid(bid_desc.start_price,bid_present),
        "cats":bidProducts.objects.values('category').distinct

    })

def minimum_bid(min_bid,present_bid):
     for bids_list in present_bid:
        if min_bid < int(bids_list.bid):
            min_bid = int(bids_list.bid)
     return min_bid

