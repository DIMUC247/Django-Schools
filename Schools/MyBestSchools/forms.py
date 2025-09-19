from django import forms
from .models import Subject, Cabinet


class SubjectForm(forms.Form):
    name = forms.CharField(
        label="Назва предмета",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


class StudentForm(forms.Form):
    first_name = forms.CharField(
        label="Ім'я",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Прізвище",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    bio = forms.CharField(
        label="Додаткова інформація про контакт",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    cabinet = forms.ModelChoiceField(
        label="Виберіть кабінет",
        queryset=Cabinet.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"})
    )
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
        label="Виберіть предмети для навчання"
    )
