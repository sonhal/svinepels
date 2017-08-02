
from django.contrib.auth.models import User
from .models import SendCoins, UserAddress
from Savoir import Savoir


rpcuser = 'multichainrpc'
rpcpasswd = '68N2Mx1sGrhhR1QTxCgBvDkXcH8me1Zu4oEXubkhfge8'
rpchost = 'localhost'
rpcport = '2768'
chainname = 'testchain'


def connect_to_blockchain():
    try:
       api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

       return api
    except:
        err = "ERROR in connection to blockchain"
        return err


def get_info():
    api = connect_to_blockchain()
    try:
       nodeinfo = api.getinfo()
    except:
       nodeinfo = "ERROR"
    return nodeinfo


def get_user_address(request):
    try:
        uaddress = UserAddress.objects.get(pk=request.user.id)
        return str(uaddress.address)
    except:
        return "ERROR"


def get_user_balance(user_address):
    api = connect_to_blockchain()
    try:
       balance = api.getaddressbalances(user_address)
       bal = balance[0]
       return bal
    except:
        balance = {'qty' : "ERROR getting user balance"}
        return balance


def send_coins(from_address, to_address, amount):
    to_user = UserAddress.objects.get(pk=to_address[0])
    amount_int = int( '0' + amount)
    api = connect_to_blockchain()
    send = api.sendassetfrom(from_address,to_user.address,"Svinepelser",amount_int )
    debug_info = { 'send' : send , 'fra' : from_address }
    return debug_info

def blockchain_make_address(user):
    api = connect_to_blockchain()
    address = api.getnewaddress()
    new_user = UserAddress.objects.create(user=user, address=address)
    new_user.save()
    return new_user