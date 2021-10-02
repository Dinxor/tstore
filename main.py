from tkinter import Tk, Button, Label
from threading import Thread
from queue import Queue
import configparser
import sys
import os


def init_config(path):
    config.optionxform = str
    config.read(path)


def maingui():
    for name in tt['modules'].keys():
        tt[name]['label'].config(text=str(tt[name].get('cnt', 0)),
                                 bg=('lime' if (tt[name].get('is_working', False)) else 'white'))
    root.after(1000, maingui)


def rstart(name):
    if not tt[name].get('is_enable', True):
        tt[name].update({'is_enable': True})
    elif not tt[name].get('is_enable', False):
        tt[name].update({'is_enable': True})
        thread = Thread(target=eval(name), args=(tt,))
        thread.daemon = True
        thread.start()


def rstop(name):
    if tt[name].get('is_enable', False):
        tt[name].update({'is_enable': False})


if __name__ == '__main__':
    root = Tk()
    root.geometry('+200+200')
    root.overrideredirect(0)
    # uncomment for minimize
    # root.iconify()
    tt = {}
    modules = []
    if len(sys.argv) < 2:
        path = './settings.ini'
    else:
        print(sys.argv[1])
        path = './%s' % (sys.argv[1])
    if not os.path.exists(path):
        print('Settings file %s not found' % (path))
        sys.exit()
    config = configparser.ConfigParser()
    init_config(path)
    for section in config.sections():
        tt.update({section.lower():dict(config[section])})
        if section == 'MODULES':
            for key in config[section]:
                modules.append([key, config[section][key]])
                exec('from modules.%s import %s' % (key, key))
    for [name, autostart] in modules:
        module = tt.get(name, {})
        q = Queue()
        module.update({'queue': q})
        module.update({'cnt': 0})
        tt.update({name: module})
    for i, [name, autostart] in enumerate(modules):
        module = tt.get(name, {})
        Label(text=name).grid(row=i, column=0)
        Button(text="Start", command=lambda x=name: rstart(x)).grid(row=i, column=1)
        Button(text="Stop", command=lambda x=name: rstop(x)).grid(row=i, column=2)
        label = Label(root, bg='white', text='0')
        label.grid(row=i, column=3)
        module.update({'label': label})
        tt.update({name: module})
        if autostart:
            rstart(name)

    root.after(100, maingui)
    root.mainloop()
