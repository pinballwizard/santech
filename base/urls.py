__author__ = 'pinballwizard'

from django.conf.urls import patterns, url
from base import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^pricing', views.pricing, name='pricing'),
    url(r'^reviews', views.reviews, name='reviews'),
    url(r'^services', views.services, name='services'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^company', views.company, name='company'),
    url(r'^workers', views.workers, name='workers'),
    url(r'^robots.txt$', TemplateView.as_view(template_name='base/robots.txt'), name='robots'),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name='base/sitemap.xml'), name='sitemap'),
)