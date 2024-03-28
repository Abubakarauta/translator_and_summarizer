from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('summarizer/', summarizer, name='summarizer'),
    path('translator/', translator, name='translator'),
    path('usersProfile/', usersProfile, name='usersProfile'),
    path('faq/', faq , name='faq'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', login, name='login'), 
    path('error/', error, name='error'),
    path('blank/', blank, name='blank'),
]
