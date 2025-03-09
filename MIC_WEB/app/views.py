from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required
def home(request): 
    return render(request, "index.html")


def authView(request): 
    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:login")
    else:
        form = UserCreationForm()  

    return render(request, "registration/signup.html", {"form": form})
