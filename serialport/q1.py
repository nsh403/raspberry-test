"""
"""

import serial

print('open serial port.')
target_dev = "/dev/serial0"
#target_dev = "COM9"
sp = serial.Serial(target_dev)

print('send a message to serial port.')

for i in range(2):
    #s = "{} ".format(i)
    s = "A message from the serial port...\r\n"
    sp.write(s)
    print('sended.')

print("end")

