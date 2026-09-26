"""
PROJECT LEVEL SETTINGS
"""
from . views import  register_view,login_view,logout_view,home
from django.urls import  path
urlpatterns =[
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('',home,name='home'),
]