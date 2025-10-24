from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponseForbidden

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, LoginForm
from .models import MySuperStudent
from Schools.StudentManager import forms


# Create your views here.

def signup(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect("index")

    form = SignUpForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.success(request=request, level=messages.SUCCESS, message="Реєстрація пройшла успішно!")
        return redirect("index")
    return render(request=request, template_name="signup.html", context={"form": form})


def signin(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect("index")

    form = LoginForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request=request, user=user)
            messages.success(request=request, level=messages.SUCCESS, message="Вхід пройшов успішно!")
            return redirect("index")
    return render(request=request, template_name="signin.html", context={"form": form})
