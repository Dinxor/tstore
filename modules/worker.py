from time import sleep

def worker(tt):
    name = 'worker'
    sleep(1)
    cnt = 0
    source = tt[name].get('queue')
    while 1:
        if not tt[name].get('is_working', False) and tt[name].get('is_enable', False):
            tt[name].update({'is_working':True})
        elif tt[name].get('is_working', False) and not tt[name].get('is_enable', False):
            tt[name].update({'is_working':False})
        while not source.empty():
            new_data = source.get(block=True)
            if tt[name].get('is_enable', False):
                print(new_data)
                cnt +=1
            else:
                pass
            tt[name].update({'cnt':cnt})
        sleep(1)
