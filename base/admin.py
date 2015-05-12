from django.contrib import admin
from base.models import *

from django_summernote.admin import SummernoteModelAdmin

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    model = ProjectImage
    list_display = ('project', 'header', 'text', 'image')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Review)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('owner', 'header', 'text', 'grade')

@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('header', 'image')

# @admin.register(Partner)
# class PartnerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'logo')

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'photo')

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone1', 'phone2')
    readonly_fields = ('latitude', 'longitude')

    def save_model(self, request, obj, form, change):
        obj.geocode()
        obj.save()

@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    list_display = ('name', 'pub_date')

@admin.register(SocialWidget)
class SocialWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sale')

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('sender', 'email', 'subject')
    readonly_fields = ('sender', 'email', 'subject', 'message')