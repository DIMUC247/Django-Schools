from django.contrib import admin

from .models import Student, Subject, Cabinet

# Register your models here.

admin.site.register([Student, Subject, Cabinet])
