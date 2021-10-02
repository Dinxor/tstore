import time

from channels.snap import get_float


def manager(tt):
    name = 'manager'
    tt[name].update({'is_working': True})
    direction = tt[name]['target']
    target = tt[direction]['queue']
    cnt = 0
    prev_s = 0
    
    addr = tt['plc1']['addr']
    rack = int(tt['plc1']['rack'])
    cpu = int(tt['plc1']['cpu'])
    dbnumber = int(tt['plc1']['db'])
    start = int(tt['plc1']['start'])
    amount = int(tt['plc1']['amount'])
    area = int(tt['plc1']['area'])
    plc_addr = [addr, rack, cpu]
    plc_area = [area, dbnumber, start, amount]
    while tt[name].get('is_enable', False):
        curr_s = int(time.time())
        if curr_s - prev_s > 59:
            get_float(plc_addr, plc_area, target, 'test_S7')
            prev_s = curr_s
            cnt += 1
            tt[name].update({'cnt': cnt})
        time.sleep(1)
    tt[name].update({'is_working': False})
    tt[name].pop('is_enable')
