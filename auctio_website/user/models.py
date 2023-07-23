from django.db import models



# Create your models here.

class bidProducts(models.Model):
    username=models.CharField(max_length=64)
    desc=models.TextField()
    title=models.CharField(max_length=64)
    start_price=models.IntegerField()
    image=models.CharField(max_length=200,blank=True,null=True,default=None)
    category=models.CharField(max_length=64)
    bid_active=models.BooleanField(default=True)



