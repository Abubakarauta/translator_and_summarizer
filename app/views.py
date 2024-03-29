from django.shortcuts import render, HttpResponseRedirect, redirect
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from django.contrib.auth import get_user_model 
User = get_user_model()
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')




def translator(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        source_lang = request.POST.get('source_lang', '')
        target_lang = request.POST.get('target_lang', '')

        print("this is the input the user provided:")
        print(input_text)

        print("this is the language the user wants to translate:")
        print(target_lang)

        print("this iss the source language")
        print(source_lang)

        # Perform translation using the pretrained model
        tokenizer = AutoTokenizer.from_pretrained("alirezamsh/small100")
        model = AutoModelForSeq2SeqLM.from_pretrained("alirezamsh/small100")

        tokenizer.tgt_lang = target_lang
        encoded_text = tokenizer(input_text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_text)
        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        
        print("this is the Translation:")
        print(translated_text)
        return render(request, 'translator.html', {'translated_text': translated_text[0]})
    
    return render(request, 'translator.html')



def summarizer(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')  # Assuming the input text comes from a form field named 'input_text'

            # Load the pre-trained tokenizer and model for text summarization
        tokenizer = AutoTokenizer.from_pretrained("Falconsai/text_summarization")
        model = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/text_summarization")


        # Tokenize the input text and generate the summary
        inputs = tokenizer([input_text], max_length=1024, return_tensors='pt', truncation=True)
        summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=150, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        print("this is the summary")
        print(summary)
        # Pass the summarized text to the template for display
        return render(request, 'summarizer.html', {'input_text': input_text, 'summary': summary})

    
    # If it's not a POST request, render the empty form
    return render(request, 'summarizer.html', {'input_text': '', 'summary': ''})

def usersProfile(request):
    return render(request, 'usersProfile.html')

def faq(request):
    return render(request, 'pages-faq.html')

def contact(request):
    return render(request, 'pages-contact.html')
    



def register(request):
    pass


def login(request):
    error = ""
    if request.method == "POST": # If the form has been submitted...
        username = request.POST['username']
        password = request.POST['password'] 
    
        # Check to make sure both fields are entered
        if len(username) < 1 or len(password) < 1:
            error = "Error! Both fields required."
        
        # Check that the password is not too short (minimum 6 characters)
        elif len(password) < 6:
            error = "Error! Password must be at least 6 characters long."
            
        else: # If everything's correct, then log the user in.
            request.session['logged_in'] = True
            request.session['user_name'] = username
            return HttpResponseRedirect('/index/')# Redirect user to dashboard page
             
    # User reached this page via GET (not POST) so just render the page
    else:
        return render(request, 'pages-login.html', {'error': error})
    return render(request, 'pages-login.html')


def error(request):
    return render(request, 'pages-error-404.html')


def blank(request):
    return render(request, 'pages-blank.html')