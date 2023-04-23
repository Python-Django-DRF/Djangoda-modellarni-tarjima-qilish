from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import University, Student


@admin.register(Student)
class StudentModelAdmin(TranslationAdmin):
    list_display = ("id", "first_name", "last_name", "age")
    list_display_links = ("id", "first_name", "last_name", )


@admin.register(University)
class UniversityModelAdmin(TranslationAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
