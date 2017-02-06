from django.db import models
from yandex_cash_register.interfaces import IPayableOrder
from datetime import timedelta
from django.utils import timezone

class Order(IPayableOrder, models.Model):
    order_id = models.IntegerField(default=0)
    phone = models.CharField(max_length=20, default="")
    user_id = models.CharField(max_length=100, default="")
    club = models.CharField(max_length=200, default="")
    order_type = models.CharField(max_length=100, default="")
    item_kod = models.CharField(max_length=100, default="")

    def get_absolute_url(self):
        return "/"
        """Django's method to find models absolute url"""

    def get_payment_complete_url(self, success):
        return "/"
        """Generate url to show user with provided result of payment
        :type success: bool
        :param success: whether payment succeeded or not
        :return: an URL to redirect to
        """

    @classmethod
    def get_by_order_id(cls, order_id):
        return cls.objects.get(order_id=order_id)
        """Find order associated with payment by order_id provided
        :type order_id: basestring
        :param order_id: an order id, which was saved on payment creation
        :return: An order object
        """

    def __str__(self):
        return str(self.order_id)

    def __unicode__(self):
        return str(self.order_id)
        

class Code(models.Model):
    phone = models.CharField(max_length=20)
    code = models.IntegerField()
    daterequest = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return str(self.code)

    def __str__(self):
        return str(self.code)
