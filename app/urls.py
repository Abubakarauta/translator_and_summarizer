from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('summarizer/', summarizer, name='summarizer'),
    path('translator/', translator, name='translator'),
    path('usersProfile/', view_or_edit_profile, name='usersProfile'),
    path('faq/', faq , name='faq'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', loginView, name='login'), 
    path('error/', error, name='error'),
    path('blank/', blank, name='blank'),
]
