from django.shortcuts import render
from .multichain_manager import get_info, get_user_balance
from django.contrib.auth.decorators import login_required
from .models import user_addresses
# Create your views here.

multichaininfo = get_info()

def get_user_address():
    uaddress = user_addresses.objects.get(pk=1)
    return str(uaddress.address)

balance = get_user_balance(get_user_address())


def info(request):
    return render(request, 'info.html', {'info' : multichaininfo} )

def index(request):
    return render(request, 'index.html', {'info' : multichaininfo} )

@login_required()
def user_homepage(request):
    return render(request, 'homepage.html', {'balance' : balance}  )




