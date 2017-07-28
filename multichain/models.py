from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def create_user(username,password):
    user = User.objects.create_user(username=username,password=password)

class User_addresses():
    user = models.ForeignKey(User)
    address = models.CharField(max_length=1000)
