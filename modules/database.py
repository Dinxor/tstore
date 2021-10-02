from time import sleep

import sqlalchemy as db

def database(tt):
    name = 'database'
    cnt = 0
    tt[name].update({'is_working': True})
    source = tt[name].get('queue')
    db_uri = tt[name].get('uri')
    engine = db.create_engine(db_uri)
    conn = engine.connect()
    metadata = db.MetaData()
    storage = db.Table('storage', metadata, autoload=True, autoload_with=engine)
    while tt[name].get('is_enable', False):
        while not source.empty():
            new_data = source.get(block=True)
            if tt[name].get('is_enable', False):
                if new_data[0] == 'web':
                    code, val = new_data[1]
                    conn.execute(storage.insert().values(code=code, value=val))
                    cnt += 1
            tt[name].update({'cnt': cnt})
        sleep(1)
    tt[name].update({'is_working': False})
    tt[name].pop('is_enable')
