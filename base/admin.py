from django.contrib import admin
from base.models import *

from django_summernote.admin import SummernoteModelAdmin

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('text', 'position', 'image')

@admin.register(Review)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('owner', 'header', 'text', 'grade')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('header', 'text')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')

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
    list_display = ('name', 'price')

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('sender', 'email', 'subject')
    readonly_fields = ('sender', 'email', 'subject', 'message')