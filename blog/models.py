from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField(upload_to='blog/static/img', default='')
    price_hour = models.CharField(max_length=5, default='')
    price_2hour = models.CharField(max_length=5, default='')
    price_night = models.CharField(max_length=5, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
