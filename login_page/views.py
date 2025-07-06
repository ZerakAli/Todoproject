from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required

#def login_page(request):
    # HttpResponse("")

@login_required
def home_(request):
    return render(request, "home_.html", {}) 


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page:login') 
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})




# Create your views here.
