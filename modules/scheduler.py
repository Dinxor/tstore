import os
import time
import subprocess


def scheduler(tt):
    name = 'scheduler'
    tt[name].update({'is_working': True})
    direction = tt[name]['target']
    target = tt[direction]['queue']
    cnt = 0
    prev_s = 0
    state = ''
    tasks = tt['tasks']
    while tt[name].get('is_enable', False):
        curr_s = int(time.time())
        if curr_s - prev_s > 59:
            currtime = time.strftime('%H%M')
            if currtime in tasks.keys():
                command = tasks[currtime]
                try:
                    rezult = subprocess.run([command], timeout=59, capture_output=True)
                    if rezult.returncode ==0:
                        state = 'OK'
                    else:
                        state = 'Code %s' % (rezult.returncode)
                except:
                    state = 'Timeout'
                target.put(['scheduler', [currtime, state]], block=True)
                prev_s = curr_s
                cnt += 1
        time.sleep(1)
        if state != '':
            print(state)
            state = ''
        tt[name].update({'cnt': cnt})
    tt[name].update({'is_working': False})
    tt[name].pop('is_enable')
