import os.path
from time import sleep
import sqlite3


def init_db(file):
    if os.path.isfile(file):
        conn = sqlite3.connect(file)
    else:
        conn = sqlite3.connect(file)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE storage
                    (id integer primary key autoincrement,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    code int,
                    value int)''')
        conn.commit()
    return conn


def sqlite(tt):
    name = 'sqlite'
    sleep(1)
    cnt = 0
    source = tt[name].get('queue')
    db_file = tt[name].get('filename')
    conn = init_db(db_file)
    cur = conn.cursor()
    mode = tt['modules'][name]
    if mode != '1':
        tt[name].update({'is_enable': False})
    while 1:
        if not tt[name].get('is_working', False) and tt[name].get('is_enable', False):
            tt[name].update({'is_working': True})
        elif tt[name].get('is_working', False) and not tt[name].get('is_enable', False):
            tt[name].update({'is_working': False})
        while not source.empty():
            new_data = source.get(block=True)
            if tt[name].get('is_enable', False):
                if new_data[0] == 'web':
                    code, val = new_data[1]
                    print(code, val)
                    cur.execute("INSERT INTO storage (code, value) VALUES (%s, %s)" % (code, val))
                    conn.commit()
                    cnt += 1
            else:
                pass
            tt[name].update({'cnt': cnt})
        sleep(1)
