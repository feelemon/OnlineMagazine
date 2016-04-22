from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User)
    # user = User(username=['username'], email=['email'], first_name=['email'])
    # user.save()
    # user = models.ForeignKey(User, unique=True)

    # The rest is completely up to you...
    # favorite_band = models.CharField(max_length=100, blank=True)
    # favorite_cheese = models.CharField(max_length=100, blank=True)
    # lucky_number = models.IntegerField()


    title = models.CharField(max_length=200)
    text = models.TextField()

    # user_id = user.pk

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # class Meta:
    #     permissions = (
    #         # Идентификатор права       Описание права
    #         ("can_drive",               "Может водить"),
    #         ("can_vote",                "Может голосовать на выборах"),
    #         ("can_drink",               "Может пить алкоголь"),
    #     )