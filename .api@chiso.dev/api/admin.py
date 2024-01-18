from django.contrib import admin
from .models import *
from django.conf import settings
from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    pass


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "start_date")


class ExperienceSARAdmin(admin.ModelAdmin):
    list_display = ("experience", "index", "statement")


class ProjectAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


class OTPAdmin(OTPAdminSite):
    pass


if settings.ENABLE_MFA:
    admin_site = OTPAdmin(name='OTPAdmin')
    admin_site.register(User)
    admin_site.register(TOTPDevice, TOTPDeviceAdmin)
else:
    admin_site = admin.site
    setup_admin_site = OTPAdmin(name='OTPAdmin')
    setup_admin_site.register(User)
    setup_admin_site.register(TOTPDevice, TOTPDeviceAdmin)

admin_site.register(Article, ArticleAdmin)
admin_site.register(Experience, ExperienceAdmin)
admin_site.register(ExperienceSAR, ExperienceSARAdmin)
admin_site.register(Project, ProjectAdmin)
admin_site.register(Contact, ContactAdmin)
