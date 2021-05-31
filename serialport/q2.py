"""
"""

import serial
from time import sleep

print('open serial port.')
# seport = serial.Serial("/dev/serial0", 9600)  # default bps
seport = serial.Serial("/dev/serial0", 57600)  # PMMS WS bps


def do_read():

    while True:
        s = seport.read()
        '''
        if not True:
            sleep(0.03)  # ?? nash
            cnt = sp.inWaiting()
            s += sp.read(cnt)
        else:
            pass
        '''
        print('read: ', s)
        seport.write(s)

"""
    가나다라

"""
def do_readline():
    """
        putty 
            keyboard option
            Enter key --> CR + LF

    """
    while True:
        s = seport.readline()
        print('line read: ', s)
        seport.write(s)

import math
def do_pmms():
    print('^c to break.')
    seed = 0.5
    while True:
        s = seport.readline()
        print('line read: ', s)
        # seport.write(b'->' + s)
        if s.startswith(b'*RD'):
            seed *= 1.7
            f1 = math.fmod(seed, 0.9)
            '''
            C# source
            string s1 = String.Format("ID:{0:N0},PM1.0:{1:N2},PM2.5:{2:N2},CO2:{3:N2},Temp:{4:N2},Humi:{5:N2},GPS:N035.211529/E120.860768\r\n",
                            f1 * 5, f1 * 50, (1.0 - f1) * 55, ((f1 * 8.0) % 4) * 100, f1 * 45, f1 * 20);			
            '''
            vpacket = 'ID:{0:.2f},PM1.0:{1:.2f},PM2.5:{2:.2f},CO2:{3:.2f},Temp:{4:.2f},Humi:{5:.2f},GPS:N035.000/E120.000\r\n'\
                .format(f1 * 5, f1 * 50, (1.0 - f1) * 55, ((f1 * 8.0) % 4) * 100, f1 * 45, f1 * 20)
            seport.write(bytes(vpacket, 'ascii'))


def main():
    print('start')
    
    #do_read()
    #do_readline()
    do_pmms()

    print("end")

main()
