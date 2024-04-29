from django.shortcuts import render, HttpResponseRedirect, redirect
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm





# Create your views here.

def index(request):
    is_authenticated = request.user.is_authenticated
    return render(request, 'index.html', {'is_authenticated': is_authenticated})


def translator(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        source_lang = request.POST.get('source_lang', '')
        target_lang = request.POST.get('target_lang', '')

        # Perform translation using the pretrained model
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        tokenizer = AutoTokenizer.from_pretrained("alirezamsh/small100")
        model = AutoModelForSeq2SeqLM.from_pretrained("alirezamsh/small100")

        tokenizer.tgt_lang = target_lang
        encoded_text = tokenizer(input_text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_text)
        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        print(translated_text)
        return render(request, 'translator.html', {'translated_text': translated_text[0]})
    return render(request, 'translator.html')

def summarizer(request):
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')  # where the input text comes from a form field named 'input_text'

        # Load the pre-trained tokenizer and model for text summarization
        tokenizer = AutoTokenizer.from_pretrained("Falconsai/text_summarization")
        model = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/text_summarization")


        # Tokenize the input text and generate the summary
        inputs = tokenizer([input_text], max_length=1024, return_tensors='pt', truncation=True)
        summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=150, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Pass the summarized text to the template for display
        return render(request, 'summarizer.html', {'input_text': input_text, 'summary': summary})

    
    # If it's not a POST request, render the empty form
    return render(request, 'summarizer.html', {'input_text': '', 'summary': ''})


def faq(request):
    return render(request, 'pages-faq.html')

def contact(request):
    return render(request, 'pages-contact.html')
    

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created. Please log in.')
            return redirect('/login/')  # Redirect to login page after successful registration
        else:
            # Handle form validation errors and display appropriate error messages
            if 'email' in form.errors:
                messages.error(request, 'The email address is invalid or already exists.')
            elif 'password2' in form.errors:
                messages.error(request, 'The passwords do not match.')
            else:
                messages.error(request, 'Please correct the errors below.')

    else:
        form = CustomUserCreationForm()

    return render(request, 'pages-register.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # Change to use 'email' instead of 'username'
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Use 'email' as the username
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index page after successful login
            else:
                error_message = 'Invalid email or password.'
                return render(request, 'pages-login.html', {'form': form, 'error': error_message})
    else:
        form = AuthenticationForm()
    
    return render(request, 'pages-login.html', {'form': form})

def error(request):
    return render(request, 'pages-error-404.html')


def blank(request):
    return render(request, 'pages-blank.html')



def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def view_or_edit_profile(request):
    user_profile = request.user.profile  # Assuming Profile is linked to User correctly

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()  # Let the form handle saving user and profile data
            messages.success(request, 'Profile updated successfully.')  # Add a success message
            return redirect('usersProfile')
        else:
            messages.error(request, 'Please correct the errors below.')  # Add an error message for invalid form
    else:
        form = ProfileForm(instance=user_profile)

    context = {'user_profile': user_profile, 'form': form}
    return render(request, 'usersProfile.html', context)
