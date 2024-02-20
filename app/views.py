from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def summarizer(request):
    return render(request,'summarizer.html')

def translator(request):
    return render(request, 'translator.html')   

def users_profile(request):
    return render(render, 'users-profile.html')

