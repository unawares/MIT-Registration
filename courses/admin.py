from django.contrib import admin
from django import forms

from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Speaker
from .models import Course
from .models import Registration


# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'course')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname', 'course')