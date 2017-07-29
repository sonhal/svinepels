

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


def get_user_balance(user_address):
    api = connect_to_blockchain()
    try:
       balance = api.getaddressbalances(user_address)
       bal = balance[0]
       return bal
    except:
        balance = {'qty' : "ERROR getting user balance"}
        return balance