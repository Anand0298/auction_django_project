from django.urls import path
from . import views
urlpatterns=[
   
 path("categories/<str:cat_name>", views.categories, name="category"),
 path("category",views.category_list,name="category_list"),
 path("bid", views.bid, name="bid"),
 
    
]