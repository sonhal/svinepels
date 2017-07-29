from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class user_addresses(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=100)

    def __str__(self):
        return "{0} Blockchain address".format(self.user)


def create_user(username,password):
    user = User.objects.create_user(username=username,password=password)


