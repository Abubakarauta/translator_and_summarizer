
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('summarizer', summarizer, name='summarizer'),
    path('translator', translator, name='translator'),
    path('users-profile', users_profile, name='users-profile'),
]