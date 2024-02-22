from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def summarizer(request):
    return render(request,'summarizer.html')

def translator(request):
    return render(request, 'translator.html')   

def usersProfile(request):
    return render(request, 'usersProfile.html')

def faq(request):
    return render(request, 'pages-faq.html')

def contact(request):
    return render(request, 'pages-contact.html')

def register(request):
    return render(request, 'pages-register.html')


def login(request):
    return render(request, 'pages-login.html')


def error(request):
    return render(request, 'pages-error-404.html')


def blank(request):
    return render(request, 'pages-blank.html')