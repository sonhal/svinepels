from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserAddress(models.Model):
    user = models.ForeignKey(User, related_name="blockchain_address")
    address = models.CharField(max_length=100)

    def __str__(self):
        return (self.user.username)

class SendCoins(models.Model):
    to_user = models.ForeignKey(User, related_name="received_coins")
    amount = models.IntegerField()

    def __str__(self):
        return "{0} sendt {2} to {1}".format(self.from_user.username, self.to_user.username, self.amount)

class UserAddressManager(models.Manager):
    def create_user_address(self, address):
        user_address = self.create(adress=address)

        return user_address



