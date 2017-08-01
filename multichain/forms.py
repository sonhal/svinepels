from django.forms import ModelForm
from django.forms import Form
from .models import SendCoins
from django.contrib.auth.models import User


class Send_coins_form(ModelForm):
    class Meta:
       model = SendCoins
      # fields = '__all__'
       fields = ['from_user','to_user','amount']

"""
class User_form(Form):
    users = ModelMultipleChoiceField(queryset=User.objects.all())


class register_testuser(ModelForm):
    class Meta:
       model = Test_users
       fields = ['name']
"""


