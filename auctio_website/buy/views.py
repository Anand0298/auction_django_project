from django.shortcuts import render,redirect
from .models import bidding,comments,watchlist
from buy.models import bidProducts
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from auctio_website.views import pro_page,minimum_bid
from buy.models import win

# Create your views here.

@login_required(login_url='register')
def watchlistpage(request,username):

    watch_=watchlist.objects.filter(user=username)
    return render(request,"watchlist.html",{
        "list_":watch_
    })


@login_required(login_url="register")
def addwatch(request):
    list_id=request.GET["listid"]
    _list=watchlist.objects.filter(user=request.user.username)

    for prods in _list:
      if int(prods.watch_list.id)==int (list_id):
        return watchlist(request,request.user.username)
    
    newwatch=watchlist(watch_list=bidProducts.objects.get(pk=list_id),user=request.user.username)
    newwatch.save()

    messages.success(request,"Product has been added to watchlist")

    return pro_page(request,list_id)

@login_required (login_url="register")
def deletewatch(request):
   
    remove_id=request.GET['listid']
    _list=watchlist.objects.get(pk=remove_id)

    messages.success(request,f"'{_list.watch_list.title}' is deleted from your watchlist")
    _list.delete()

    return redirect("home")

def winner(request):
   bid_id=request.GET["listid"]
   bids_present=bidding.objects.filter(pro_id=bid_id)
   print("hello")
   print(bid_id)
   biddesc = bidProducts.objects.get(pk = bid_id, bid_active = True)
   maximum_bid=minimum_bid(biddesc.start_price,bids_present)

   try:
        winner_objects=bidding.objects.get(bid=maximum_bid,pro_id=bid_id)
        winner_obj=bidProducts.objects.get(id=bid_id)
        winn=win(bid_win_list=winner_obj,username=winner_objects.user)
        winners_name = winner_objects.user
        
   except:     

        winner_obj = bidProducts.objects.get(start_price = maximum_bid, id = bid_id)
        winn = win(bid_win_list = winner_obj, username = winner_obj.username)
        winners_name = winner_obj.user

   biddesc.bid_active = False
   biddesc.save()
   
   winn.save()
   messages.success(request, f"{winners_name} won {winn.bid_win_list.title}.")
   return redirect("home")

def winnings(request):
    try:
        your_win=win.objects.filter(username=request.user.username)
    except:
        your_win=None

    return render(request,"winning.html",{
        "win_list":your_win
    })

   
   






    


