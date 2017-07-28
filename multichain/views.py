from django.shortcuts import render
from .multichain_manager import get_info
from django.contrib.auth.decorators import login_required
# Create your views here.

multichaininfo = get_info()

def info(request):
    return render(request, 'info.html', {'info' : multichaininfo} )

def index(request):
    return render(request, 'index.html', {'info' : multichaininfo} )

@login_required()
def user_homepage(request):
    return render(request, 'homepage.html' )