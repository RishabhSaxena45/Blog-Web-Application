from django.urls import path
from blog import views

urlpatterns = [
    path('' , views.loginn , name="loginn"),
    path('signup/' , views.signup , name="signup"),
    path('home/' , views.home , name="home"),
    path('newpost/' , views.newpost , name="newpost"),
    path('mypost/' , views.mypost , name="mypost"),
    path('signout/' , views.signout , name="signout"),
    path('update/<int:pk>' , views.studentupdate.as_view() , name="update")
]
