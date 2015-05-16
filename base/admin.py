from django.contrib import admin
from base.models import *

# from django_summernote.admin import SummernoteModelAdmin


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


class SocialWidgetAdmin(admin.StackedInline):
    model = SocialWidget


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        ProjectImageAdmin,
    ]


@admin.register(Review)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('owner', 'header', 'text', 'grade')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('header', 'image')


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
    inlines = [
        SocialWidgetAdmin,
    ]

    def save_model(self, request, obj, form, change):
        obj.geocode()
        obj.save()


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sale')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('sender', 'email', 'subject')
    readonly_fields = ('sender', 'email', 'subject', 'message')