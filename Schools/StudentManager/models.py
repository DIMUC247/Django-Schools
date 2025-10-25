from django.contrib.auth.models import AbstractUser
from django.db import models

class MySuperStudent(AbstractUser):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username

class SchoolClass(models.Model):
    name = models.CharField(max_length=100, unique=True)
    amount_of_students = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name