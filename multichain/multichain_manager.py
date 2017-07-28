

from Savoir import Savoir


rpcuser = 'multichainrpc'
rpcpasswd = '68N2Mx1sGrhhR1QTxCgBvDkXcH8me1Zu4oEXubkhfge8'
rpchost = 'localhost'
rpcport = '2768'
chainname = 'testchain'

def get_info():
    api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
    nodeinfo = api.getinfo()
    return nodeinfo

