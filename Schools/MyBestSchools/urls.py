from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add_subject/", views.add_subject, name="add_subject"),
    path("subjects/", views.get_subjects, name="get_subjects"),
    path("students/", views.get_students, name="get_students"),
    path("add_student/", views.add_student, name="add_student")
]