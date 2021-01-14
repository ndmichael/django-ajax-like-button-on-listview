from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post (models.Model):

    STATUS_POST = (
        ('published', 'Published'),
        ('status', 'Status'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to='post_images/%Y/%m/%d', default="",  blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_POST, default='published')
    likes = models.ManyToManyField(User,related_name='user_like', blank=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title}"
