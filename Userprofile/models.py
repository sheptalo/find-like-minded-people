from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfileModel(models.Model):

    user_main = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_date = models.DateTimeField()

    def __str__(self):
        return self.user_main.username
