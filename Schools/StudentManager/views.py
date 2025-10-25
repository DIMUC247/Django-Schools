from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponseForbidden

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, LoginForm
from . import forms
from .models import MySuperStudent
# from Schools.StudentManager import forms


# Create your views here.
def index(request):
    student = request.user if request.user.is_authenticated else None
    return render(request, "index.html", {"student": student})


def signup(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect("index")

    form = SignUpForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request=request, user=user)
        messages.add_message(request, messages.SUCCESS, "Реєстрація пройшла успішно!")
        return redirect("index")
    return render(request=request, template_name="sign_up.html", context={"form": form})


def signin(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("index")

    form = LoginForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
    return render(request=request, template_name="sign_in.html", context={"form": form})


@login_required
def signout(request: HttpRequest):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Ви успішно вийшли!")
    return redirect("index")



@login_required
def get_students(request: HttpRequest):
    return render(
        request=request,
        template_name="students.html",
        context=dict(students=MySuperStudent.objects.all())
    )