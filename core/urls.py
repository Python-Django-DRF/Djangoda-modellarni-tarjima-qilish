from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns

from django.contrib.auth.forms import AuthenticationForm
from captcha import fields

from .schema import swagger_urlpatterns


class LoginForm(AuthenticationForm):
    captcha = fields.ReCaptchaField()

    def clean(self):
        captcha = self.cleaned_data.get("captcha")
        if not captcha:
            return
        return super().clean()


admin.site.login_form = LoginForm
admin.site.login_template = "login.html"

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    re_path(r"^rosetta/", include("rosetta.urls")),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
