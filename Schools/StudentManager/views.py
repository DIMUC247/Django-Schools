from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponseForbidden

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, LoginForm, ClassForm
from . import forms
from .models import MySuperStudent, SchoolClass
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
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
    return render(request=request, template_name="sign_in.html", context={"form": form})


@login_required
def signout(request):
    if request.method == "POST" or request.method == "GET":
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Ви успішно вийшли з акаунта.")
        else:
            messages.info(request, "Ви не зареєстровані або не увійшли.")
    return redirect("index")



@login_required
def get_students(request: HttpRequest):
    return render(
        request=request,
        template_name="students.html",
        context=dict(students=MySuperStudent.objects.all())
    )


@login_required
def add_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            cls = form.save()
            messages.success(request, f"Клас '{cls.name}' додано.")
            return redirect("get_classes")
    else:
        form = ClassForm()
    return render(request, "add_class.html", {"form": form})


@login_required
def get_classes(request):
    classes = SchoolClass.objects.all().order_by("name")
    return render(request, "classes.html", {"classes": classes})


@login_required
def add_student_to_class(request, class_id):
    try:
        school_class = SchoolClass.objects.get(id=class_id)
    except SchoolClass.DoesNotExist:
        return HttpResponseForbidden("Клас не знайдено.")

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        try:
            student = MySuperStudent.objects.get(name=first_name)
            student.class_name = school_class.name
            student.save()
            messages.success(request, f"Студента '{student}' додано до класу '{school_class.name}'.")
            return redirect("get_classes")
        except MySuperStudent.DoesNotExist:
            messages.error(request, "Студента не знайдено.")

    students = MySuperStudent.objects.filter(class_name__isnull=True)
    return render(request, "add_student_to_class.html", {"school_class": school_class, "students": students})


