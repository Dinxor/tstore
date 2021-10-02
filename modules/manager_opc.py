import time

from channels.opc import opc_client, get_opc_data


def manager(tt):
    name = 'manager'
    tt[name].update({'is_working': True})
    saver_input = tt['saver']['queue']
    cnt = 0
    prev_s = 0
    state1 = 3
    
    url = tt['opc']['url']
    nodes_ = tt['opc']['nodes']
    nodes = list(nodes_.split(','))
    
    while tt[name].get('is_enable', False):
        if state1 > 0:
            conn1 = opc_client(url)
        curr_s = int(time.time())
        if curr_s - prev_s > 59:
            state1 = get_opc_data(conn1, nodes, saver_input, 'opc')
            prev_s = curr_s
            cnt += 1
            tt[name].update({'cnt': cnt})
        time.sleep(1)
    conn1.disconnect()
    tt[name].update({'is_working': False})
    tt[name].pop('is_enable')
