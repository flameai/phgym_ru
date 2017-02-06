# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.dispatch import receiver
from django.core.mail import mail_admins
from django.db.models.signals import post_save
from yandex_cash_register.models import Payment
from .models import Order
import requests
import json

@receiver(post_save, sender=Payment)
def my_callback(instance, **kwargs):
    if instance.state == "success":
        # instance - responce yandex.kassa after success payment
        order = Order.objects.get(order_id=instance.order_id)
        data = {
            "phone": order.phone,
            "user_id": order.user_id,
            "club": order.club,
            "type": order.order_type,
            "item_kod": order.item_kod,
            "amount": str(instance.order_sum),
            "customer_id": str(instance.customer_id),
            "order_id": instance.order_id,
        }

        url = "https://api.wge.ru/sportclub/hs/fitnes_mob/payment"

        r = requests.post(url,json=data)

        mail_admins("Test",r.text,fail_silently=False)
