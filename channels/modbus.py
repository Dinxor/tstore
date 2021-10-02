import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp, hooks


def modb(host, port):
    def on_before_connect(args):
        master._host = host
        master._port = port

    hooks.install_hook("modbus_tcp.TcpMaster.before_connect", on_before_connect)

    def on_after_recv(args):
        response = args[1]

    hooks.install_hook("modbus_tcp.TcpMaster.after_recv", on_after_recv)

    try:
        master = modbus_tcp.TcpMaster()
        master.set_timeout(5.0)
        return master
    except Exception as msg:
        print('error', msg)
        return ''


def get_data(conn, start, amount, target, label):
    try:
        rez = list(conn.execute(1, cst.READ_HOLDING_REGISTERS, start, amount))
        target.put([label, rez], block=True)
    except:
        return 1
    return 0
