from modeltranslation.translator import TranslationOptions, register
from .models import Student, University


@register(Student)
class StudentTranslationOptions(TranslationOptions):
    fields = ("first_name", "last_name")


@register(University)
class UniversityTranslationOptions(TranslationOptions):
    fields = ("name",)
