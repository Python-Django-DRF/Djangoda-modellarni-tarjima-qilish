from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


class Student(TimeStampedModel):
    first_name = models.CharField(_('First name'), max_length=150)
    last_name = models.CharField(_('Last name'), max_length=150)
    age = models.PositiveIntegerField(_('Age'))
    university = models.ForeignKey('test_app.University', on_delete=models.CASCADE, verbose_name=_('University'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')


class University(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('University')
        verbose_name_plural = _('Universities')
