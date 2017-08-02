from django.shortcuts import render, redirect
from .multichain_manager import get_info, get_user_balance, send_coins, get_user_address, blockchain_make_address
from django.contrib.auth.decorators import login_required
from .models import UserAddress
from .forms import Send_coins_form, RegisterForm
from django.contrib.auth.models import User


# Create your views here.

multichaininfo = get_info()


def info(request):
    return render(request, 'info.html', {'info' : multichaininfo} )

def index(request):
    return render(request, 'index.html', {'info' : multichaininfo} )

def register(request):
    ERROR = "Noe gjekk feil under registreringer, Vennligst prøv igjen"

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register' , {'info' : ERROR})
    else:
        form = RegisterForm()
    return render(request, 'register.html' , {'form' : form})

@login_required()
def make_address(request):
    if request.method == 'POST':

        user = request.user
        address = blockchain_make_address(user)
        if address != "ERROR":
            return redirect('homepage')
        else:
            return render(request, 'index.html', {'info': info})

    return render(request, 'makeaddress.html')


@login_required()
def user_homepage(request):
    balance = get_user_balance(get_user_address(request))
    user_address = get_user_address(request)
    if user_address == "ERROR":
        return redirect('makeaddress')
    else:
        if request.method == 'POST':
            form_data = request.POST
            form = Send_coins_form(data=request.POST)
            if form.is_valid():
                form.save()
                send_info = send_coins(to_address=form_data['to_user'], from_address=user_address,
                                       amount=form_data['amount'])
                return render(request, 'homepage.html', {'balance': balance, 'form': form, 'send_info': send_info})
            else:
                return render(request, 'index.html', {'info': info})
        else:
            form = Send_coins_form()
        return render(request, 'homepage.html', {'balance': balance, 'form': form})





