from opcua import Client

def opc_client(url):
    try:
        client = Client(url)
        client.connect()
        return client
    except:
        return ''

def get_opc_data(conn, nodes, target, label):
    try:
        rezult = []
        for node in nodes:
            channel = conn.get_node(node)
            rez = channel.get_value()
            rezult.append(rez)
        target.put([label, rezult], block=True)
    except:
        return 1
    return 0
