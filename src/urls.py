"""yashankin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from mainapp.sitemap import sitemaps
from django.views.decorators.cache import cache_page


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^oferta/', include('oferta.urls')),
    url(r'^shop/', include('plastic.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('mainapp.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="mainapp/robots.txt", content_type="text/plain")),
    url(r'^sitemap\.xml$', cache_page(86400)(sitemap), {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
handler404 = 'mainapp.views.handler404'
