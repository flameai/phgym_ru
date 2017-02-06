from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^money/', include('yandex_cash_register.urls',
        namespace='yandex_cash_register',
        app_name='yandex_cash_register')),
    url(r'^payment', views.payment, name='payment'),
    url(r'^send_register_email', views.send_email, name='send_email'),
    url(r'^send_sms', views.send_sms, name="send_sms"),
    url(r'^check_pin', views.check_pin, name="check_pin"),
]
