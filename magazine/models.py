from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


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
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    key_words = models.CharField(max_length=100)
    last_date = models.DateTimeField(
        default=timezone.now)


class Backet(models.Model):
    profile = models.ManyToManyField(Profile)
    product = models.CharField(Product, max_length=200)
    quantity = models.CharField(Product, max_length=200)
    # all_cost = models.IntegerField(sum(Product,))

class Order(models.Model):
    client = models.ManyToManyField(Profile, max_length=200)
    date_order = models.DateField()
    date_buy = models.DateField()
    metod = models.CharField(max_length=200, default="PayPal")
    cost = models.IntegerField()


class Post(models.Model):
    author = models.ManyToManyField(Profile)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.FileField(null=True, blank=True)
    # cost = models.IntegerField(label='cost',  max_length=5)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})