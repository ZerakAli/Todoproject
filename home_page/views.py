from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required

def home_page(request): 
   return render(request, "home__.html")  
# Create your views here.
