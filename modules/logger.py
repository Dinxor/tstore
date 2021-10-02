from time import sleep, strftime
import time

def logname():
    return strftime('%Y%m%d')+'.txt'


def logger(tt):
    name = 'logger'
    cnt = 0
    logfile = None
    source = tt[name]['queue']
    mode = tt['modules'][name]
    if mode != '1':
        tt[name].update({'is_enable': False})
    while 1:
        if not tt[name].get('is_working', False) and tt[name].get('is_enable', False):
            tt[name].update({'is_working':True})
        elif tt[name].get('is_working', False) and not tt[name].get('is_enable', False):
            tt[name].update({'is_working':False})
        while not source.empty():
            new_data = source.get(block=True)
            if tt[name].get('is_enable', False):
                if logfile == None:
                    logfile = open('./logs/'+logname(), 'a')
                str = '%s %s' % (new_data[0], new_data[1])
                logfile.write(str + '\n')
                cnt += 1
        else:
            if logfile != None:
                logfile.close()
                logfile = None
                tt[name].update({'cnt':cnt})
            sleep(1)

if __name__ == '__main__':
    print(logname())
