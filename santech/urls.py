from django.conf.urls import include, url
from django.contrib import admin
from base import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/article=(?P<article>[0-9]+)/', views.blog_article, name='blog_article'),
    url(r'^pricing/', views.pricing, name='pricing'),
    url(r'^reviews/', views.reviews, name='reviews'),
    url(r'^services/$', views.services, name='services'),
    url(r'^services/article=(?P<article>[0-9]+)/', views.services_article, name='services_article'),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^workers/', views.workers, name='workers'),
    # url(r'^summernote/', include('django_summernote.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='base/robots.txt'), name='robots'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
