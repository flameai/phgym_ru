# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie

from decimal import Decimal
from random import randrange
import datetime
import requests
import json

from yandex_cash_register.models import Payment, CashRegister
from yandex_cash_register import conf
from mainapp.models import Club

from .models import Order, Code
from . import signals


@ensure_csrf_cookie
def index(request):
    context = {"title": "Продажа абонементов"}
    return render(request, 'plastic/index.html', context)


def payment(request):
    phone = request.POST.get('phone')
    item_kod = request.POST.get('item_kod')
    user_id = request.POST.get('user_id')
    email = request.POST.get('email')
    club = request.POST.get('club')
    club_code = request.POST.get('club_code')
    order_type = request.POST.get('order_type')

    try:
        # r = requests.get('https://api.wge.ru/sportclub/hs/fitnes_mob/clubs/', \
        r = requests.get('http://2017test.u46521.netangels.ru/static/plastic/clubs.json', \
                         headers={"Content-Type": "application/json"}, verify=False)
        r.encoding = 'utf-8'
        txt = u''.join(r.text).replace("\r\n", "").replace("\xa0", "").replace("\ufeff", "")
        clubs = json.loads(txt)
        for obj in clubs['clubs']:
            if obj['club'] == club:
                for good in obj['goods']:
                    if good['item_kod'] == item_kod:
                        price = good['price']
                        price = price.replace(" ", "")
    except:
        price = 0

    try:
        order_id = int(Payment.objects.first().order_id) + 1
    except:
        order_id = 1

    club_obj = Club.objects.get(code=club_code)

    payment = Payment(
        order_sum=Decimal(price),
        order_id=order_id,
        cps_phone=phone,
        cps_email=email,
        payment_type='AC',
        cash_register=club_obj.cash_register
    )

    payment.save()

    order = Order(
        order_id=order_id,
        phone=phone,
        user_id=user_id,
        club=club,
        order_type=order_type,
        item_kod=item_kod,
    )

    order.save()

    form = payment.form()

    return render(request, 'plastic/payment.html', {'form': form, 'url': conf.TARGET})


def save_code(phone, pin):
    try:
        code = Code(
            phone=phone,
            code=pin,
        )
        code.save()
        return True
    except:
        return False


def check_pin(request):
    pin = request.GET.get('pin')
    phone = request.GET.get('phone')
    # try:
    code = Code.objects.filter(daterequest__gt=timezone.now() - datetime.timedelta(minutes=5), phone=phone).last()
    if int(pin) == code.code:
        code.delete()
        return JsonResponse({"status": "ok"})
    else:
        return JsonResponse({"status": "invalid"})
    # except:
    #     return JsonResponse({"status": "error"})


def send_email(request):
    email = request.POST.get('email')
    subject = u'Регистрация на сайте plastic.yashankin.com'
    msg = u"Текст регистрации"
    send_mail(subject, msg, settings.EMAIL_HOST_USER ,[email])
    return HttpResponse('success')


def send_sms(request):
    phone = request.POST.get('phone')
    pin = str(randrange(1000,9999))
    save_code(phone,pin)
    data = {
        "login": settings.SMS_LOGIN,
        "pass": settings.SMS_PASS,
        "from": settings.SMS_FROM,
        "to": phone,
        "text": u"Код для авторизации: " + pin
    }
    r = requests.get(settings.SMS_URL, params=data)
    return HttpResponse(r.text)
