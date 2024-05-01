from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class MyModel(models.Model):
    field_name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self): return self.title

    # def get_absolute_url(self): return reverse('main_page', args=[self.id])
