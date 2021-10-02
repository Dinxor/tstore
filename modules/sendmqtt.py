from time import sleep

import paho.mqtt.client as mqtt

def sendmqtt(tt):
    name = 'sendmqtt'
    cnt = 0
    ip=tt['mqtt1']['ip']
    port=int(tt['mqtt1']['port'])
    timeout=int(tt['mqtt1']['timeout'])
    username=tt['mqtt1']['username']
    password=tt['mqtt1']['password']
    source = tt[name].get('queue')
    client = mqtt.Client()
    client.username_pw_set(username=username,password=password)
    while 1:
        if not tt[name].get('is_working', False) and tt[name].get('is_enable', False):
            tt[name].update({'is_working':True})
        elif tt[name].get('is_working', False) and not tt[name].get('is_enable', False):
            tt[name].update({'is_working':False})
        try:
            client.connect(ip,port,timeout)
            while not source.empty():
                new_data = source.get(block=True)
                if tt[name].get('is_enable', False):
                    topic, val = new_data
                    client.publish(topic,val,qos=0,retain=True)
                    cnt +=1
                    tt[name].update({'cnt':cnt})
                else:
                    pass
            sleep(1)
        except:
            sleep(5)
