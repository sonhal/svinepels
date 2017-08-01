from django.shortcuts import render, redirect
from .multichain_manager import get_info, get_user_balance, send_coins
from django.contrib.auth.decorators import login_required
from .models import UserAddress
from .forms import Send_coins_form
from django.contrib.auth.models import User


# Create your views here.

multichaininfo = get_info()
"""
def get_user_address():
    uaddress = user_addresses.objects.get(pk=1)
    return str(uaddress.address)

balance = get_user_balance(get_user_address())
"""
balance ="sdasd"
def info(request):
    return render(request, 'info.html', {'info' : multichaininfo} )

def index(request):
    return render(request, 'index.html', {'info' : multichaininfo} )

@login_required()
def user_homepage(request):

    if request.method == 'POST':
        form_data = request.POST

        form = Send_coins_form(data=request.POST)
        if form.is_valid():
            form.save()
            send_coins(to_address=form_data['to_user'], from_address=form_data['from_user'], amount=form_data['amount'])
            return render(request, 'index.html', {'info': info})
        else:
            return render(request, 'index.html', {'info': info})
    else:
        form = Send_coins_form()
    return render(request, 'homepage.html', {'balance': balance, 'form' : form})



