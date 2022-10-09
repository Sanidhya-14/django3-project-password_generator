from http.client import HTTPResponse
from urllib import request
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import random

def home(response):
    return render(response,'generator/home.html')

def panner(response):
    return(HttpResponse("<h1>PANNER IS VeRY TASTY !!</h1>"))

def sani(response):
    return render(response,'generator/sani.html')

def password(response):
    thepassword =''
    chara=list('abcdefghijklmnopqrstuvwxyz')
    if response.GET.get('uppercase'):
        chara.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if response.GET.get('spcharacter'):      
        chara.extend(list('!@#$%^&*()'))

    if response.GET.get('numbers'):
        chara.extend(list('123456789'))          
    length=int(response.GET.get('length','8'))

    for i in range (length):
        thepassword+=random.choice(chara)
    return render(response,'generator/generator.html',{'password':thepassword})    

def about(response):
    return(render(response,'generator/about.html'))