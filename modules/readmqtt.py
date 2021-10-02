from time import sleep

import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    target = userdata['target']
    target.put(['mqtt', [str(message.topic), str(message.payload.decode("utf-8"))]], block=True)


def readmqtt(tt):
    name = 'readmqtt'
    tt[name].update({'is_working':True})
    tt[name].update({'cnt':0})
    saver_input = tt['saver']['queue']
    ip=tt['mqtt1']['ip']
    port=int(tt['mqtt1']['port'])
    timeout=int(tt['mqtt1']['timeout'])
    username=tt['mqtt1']['username']
    password=tt['mqtt1']['password']
    read_topic=tt['mqtt1']['read_topic']
    mq_userdata = {'target':saver_input}
    client = mqtt.Client(userdata=mq_userdata)
    client.on_message=on_message
    client.username_pw_set(username=username,password=password)
    while tt[name].get('is_enable', False):
        try:
            client.connect(ip,port,timeout)
            client.subscribe(read_topic)
            client.loop_start()
            while tt[name].get('is_enable', False):
                sleep(1)
        except:
            sleep(5)
    client.loop_stop()
    client.disconnect()
    tt[name].update({'is_working':False})
    tt[name].pop('is_enable')
