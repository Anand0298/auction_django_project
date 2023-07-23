from django.urls import path
from . import views
urlpatterns=[
   
    path("login", views.loginview, name="login"),
    path('register', views.register, name='register'),
    path('logout',views.logoutview,name='logout'),
    path('selling',views.sell,name="sell"),
    path('comments',views.all_comments,name="comments"),
    
]