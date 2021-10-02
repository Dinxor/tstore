import time

def manager(tt):
    name = 'manager'
    tt[name].update({'is_working': True})
    direction = tt[name]['target']
    target = tt[direction]['queue']
    cnt = 0
    prev_s = 0
    while tt[name].get('is_enable', False):
        curr_s = int(time.time())
        if curr_s - prev_s > 59:
            tstamp = time.strftime("%d.%m.%Y %H:%M:%S")
            target.put(['manager', tstamp], block=True)
            prev_s = curr_s
        time.sleep(1)
        cnt += 1
        tt[name].update({'cnt': cnt})
    tt[name].update({'is_working': False})
    tt[name].pop('is_enable')
