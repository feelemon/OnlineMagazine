from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Post(models.Model):
    author = models.ForeignKey(User)
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



    # class Meta:
    #     permissions = (
    #         # Идентификатор права       Описание права
    #         ("can_drive",               "Может водить"),
    #         ("can_vote",                "Может голосовать на выборах"),
    #         ("can_drink",               "Может пить алкоголь"),
    #     )