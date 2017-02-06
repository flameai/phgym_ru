from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^(?P<slug>[\w-]+)/news/$', views.news, name='news'),
    url(r'^(?P<slug>[\w-]+)/stock/$', views.stock, name='stock'),
    url(r'^(?P<slug>[\w-]+)/topfitness/$', views.fitness, name='fitness'),
    url(r'^(?P<slug>[\w-]+)/service/$', views.service, name='service'),
    url(r'^(?P<slug>[\w-]+)/schedule/(?P<detail>[\w-]+)$', views.schedule, name="schedule"),
    url(r'^(?P<slug>[\w-]+)/trainers/$', views.trainers, name="trainers"),
    url(r'^(?P<slug>[\w-]+)/comments/$', views.comments, name="comments"),
    url(r'^(?P<slug>[\w-]+)/about/$', views.about, name="about"),
    url(r'^(?P<slug>[\w-]+)/contacts/$', views.contacts, name="contacts"),
    url(r'^(?P<slug>[\w-]+)/call/$', views.call, name='call'),
    url(r'^(?P<slug>[\w-]+)/entry/$', views.entry, name='entry'),
    url(r'^(?P<slug>[\w-]+)/abonement/$', views.abonement, name='abonement'),

    url(r'^pages/(?P<slug>[\w-]+)/$',views.page,name='page'),

    url(r'^(?P<slug>[\w-]+)/$', views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
