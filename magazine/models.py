from django.db import models
from datetime import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import random
import string
from paypal.standard.ipn.signals import payment_was_successful
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # WARNING !
        # Check that the receiver email is the same we previously
        # set on the business field request. (The user could tamper
        # with those fields on payment form before send it to PayPal)
        if ipn_obj.receiver_email != "feelemon-facilitator_api1.bk.ru":
            # Not a valid payment
            return

        # ALSO: for the same reason, you need to check the amount
        # received etc. are all what you expect.

        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "Upgrade all users!":
            Users.objects.update(paid=True)

valid_ipn_received.connect(show_me_the_money)
#
# def show_me_the_money(sender, **kwargs):
#     ipn_obj = sender
#     if ipn_obj.custom == "upgrade all users!":
#         Users.object.update(paid = True)
#     payment_was_successful.connect(show_me_the_money)

class Users(models.Model):
    paid = False
# def my_callback(sender, **kwargs):
#     ipn_obj = sender
#     # You need to check 'payment_status' of the IPN
#     if ipn_obj.payment_status == "Completed":
#         send_mail('Subject here', 'Here is the message', 'mail@mail.com',
#         ['mail@mail.com'], fail_silently=False)
#
#
#     payment_was_successful.connect(my_callback)
# from paypal.standard.models import ST_PP_COMPLETED


# def show_me_the_money(sender, **kwargs):
#     ipn_obj = sender
#     if ipn_obj.payment_status == ST_PP_COMPLETED:
#         # WARNING !
#         # Check that the receiver email is the same we previously
#         # set on the business field request. (The user could tamper
#         # with those fields on payment form before send it to PayPal)
#         if ipn_obj.receiver_email != "feelemon@bk.ru":
#             # Not a valid payment
#             return True
#
#         # ALSO: for the same reason, you need to check the amount
#         # received etc. are all what you expect.
#
#         # Undertake some action depending upon `ipn_obj`.
#         if ipn_obj.custom == "Upgrade all users!":
#             User.objects.update(paid=True)
#         return True

class Profile(models.Model):
    nik_name = models.CharField('nik_name', max_length=300)
    password = models.CharField(max_length=50)
    address = models.CharField( max_length=50)
    date_register = models.DateTimeField(
        default=timezone.now)
    first_name = models.CharField('first_name', max_length=30)
    last_name = models.CharField('second_name', max_length=30)
    telephone_number = models.CharField(max_length=20)
    email = models.EmailField('E-mail', blank=True)
    cart_number = models.CharField(max_length=50)


class Product(models.Model):
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    quantity = models.IntegerField()
    tag = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название Категории')
    alias = models.SlugField(verbose_name='Alias категории')


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return 'Категория %s' % self.name


class Order(models.Model):
    owner = models.ForeignKey('auth.User')
    phone = models.CharField(max_length=255, verbose_name='Телефон заказчика')
    order = models.CharField(max_length=255, verbose_name='Что заказали')
    sum = models.IntegerField(default=0, verbose_name='Сумма заказа')
    last_deal = models.DateField(verbose_name='Время заказа')

    payment = models.BooleanField(default=False)

    def sum(self):
        summa = 0
        for item in self.item_set.all():
            summa += item.item.cost
        return summa

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ на %s' % self.sum

#

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, verbose_name='Название Товара')
    text = models.TextField()
    cost = models.IntegerField(default=0, verbose_name='Цена')
    image = models.FileField(null=True, blank=True)
    # cost = models.IntegerField(label='cost',  max_length=5)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    alias = models.SlugField(verbose_name='Alias товара')

    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_add = models.DateTimeField(default=timezone.now())
    col = models.IntegerField(default=1)

    def total(self):
        return self.cost * self.col
