from django.db import models
from user.models import bidProducts


class bidding(models.Model):
    bid=models.IntegerField()
    pro_id=models.IntegerField()
    user=models.CharField(max_length=80)

class comments(models.Model):
    pro_id=models.IntegerField()
    comment=models.TextField()
    user=models.CharField(max_length=80)

class watchlist(models.Model):
    watch_list = models.ForeignKey(bidProducts, on_delete=models.CASCADE)
    user = models.CharField(max_length=64)


class win(models.Model):
    bid_win_list=models.ForeignKey(bidProducts,on_delete=models.CASCADE,related_name='buy_bid')
    username=models.CharField(max_length=100,default=None)





