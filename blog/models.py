from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post (models.Model):

    title = models.CharField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to='post_images/%Y/%m/%d', default="",  blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
