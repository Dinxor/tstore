import time

from channels.modbus import modb, get_data


def manager(tt):
    name = 'manager'
    tt[name].update({'is_working': True})
    direction = tt[name]['target']
    target = tt[direction]['queue']
    cnt = 0
    prev_s = 0
    state1 = 3
    
    addr = tt['plc2']['addr']
    port = int(tt['plc2']['port'])
    start = int(tt['plc2']['start'])
    amount = int(tt['plc2']['amount'])
    
    while tt[name].get('is_enable', False):
        if state1 > 0:
            conn1 = modb(addr, port)

        if curr_s - prev_s > 59:
            state1 = get_data(conn1, start, amount, target, 'modbus')
            prev_s = curr_s
            cnt += 1
            tt[name].update({'cnt': cnt})
        time.sleep(1)
    conn1.close()
    tt[name].update({'is_working': False})
    tt[name].pop('is_enable')
