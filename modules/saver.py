from time import sleep

from modules.param import par

def saver(tt):
    name = 'saver'
    cnt = 0
    tt[name].update({'is_working': True})
    source = tt[name]['queue']
    direction = tt[name]['target']
    target = tt[direction]['queue']
    while tt[name].get('is_enable', False):
        while not source.empty():
            new_data = source.get(block=True)
            if new_data[0] == 'temp':
                rez = new_data[1]
                for i in range(len(rez)):
                    param = par.get(i, '')
                    if param != '':
                        val = str(rez[i])
                        topic = param['topic']
                        target.put([topic, val], block=True)
            cnt +=1
            tt[name].update({'cnt': cnt})
        sleep(1)
    tt[name].update({'is_working': False})
    tt[name].pop('is_enable')
