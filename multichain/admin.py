from django.contrib import admin
from .models import UserAddress,SendCoins
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(UserAddress)
admin.site.register(SendCoins)
