import pyTigerGraph as tg
from config import host, un, graph, pw

hostname = host
username = un
graphname = graph
password = pw
conn = None


def getConnection():
    try:
        conn = tg.TigerGraphConnection(host=hostname,
                                    graphname=graphname,
                                    username=username,
                                    password=password,
                                    useCert=False, 
                                    version='3.0.5'
                                    ) 
    except Exception as e:
        print(e)
        print('There was an error. Make sure to start your box and try again')
    try:
        secret = conn.createSecret()
        token = conn.getToken(secret, setToken=True)
        
                 
    except Exception as e:
        print(e)
        print('There was an error. Make sure to start your box and try again')
    return conn   

