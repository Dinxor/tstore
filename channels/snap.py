import snap7
import struct

def get_float(plc_addr, plc_area, target, label):
    try:
        plc = snap7.client.Client()
        plc.connect(*plc_addr)
        rezult = plc.read_area(*plc_area)
        plc.disconnect()
        rez = []
        for i in range(0, len(rezult), 4):
            f = int.from_bytes([rezult[x] for x in range (i, i+4)], byteorder='big')
            tval = struct.unpack('f', struct.pack('I', f))[0]
            rez.append(round(tval, 2))
        target.put([label, rez], block=True)
    except:
        return 1
    return 0


def get_int(plc_addr, plc_area, target, label):
    try:
        plc = snap7.client.Client()
        plc.connect(*plc_addr)
        rezult = plc.read_area(*plc_area)
        plc.disconnect()
        rez = []
        for i in range(0, len(rezult), 2):
            f = int.from_bytes([rezult[x] for x in range (i, i+2)], byteorder='big')
            rez.append(f)
        target.put([label, rez], block=True)
    except:
        return 1
    return 0
