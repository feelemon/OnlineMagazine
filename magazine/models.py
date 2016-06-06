from django.db import models
from datetime import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import random
import string


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
    name = models.CharField(max_length=255, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=255, verbose_name='Телефон заказчика')
    order = models.CharField(max_length=255, verbose_name='Что заказали')
    sum = models.IntegerField(default=0, verbose_name='Сумма заказа')
    last_deal = models.DateField(default= datetime.now(), verbose_name='Время заказа')


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ на %s' % self.sum

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