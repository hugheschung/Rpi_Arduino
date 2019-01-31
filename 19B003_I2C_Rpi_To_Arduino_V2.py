import smbus
import time

bus = smbus.SMBus(1)


def writeNumber(address, value):
    bus.write_byte(address, value)
    return -1

def readNumber(address):
    number = bus.read_byte(address)
    return number

while True:
    address = input('請輸入位址： ')
    var = input('Enter 1 – 9: ')

    writeNumber(int(address),int(var))
    print ('RPI: Hi Arduino, I sent you ', var)
    # 等待1秒
    time.sleep(1)
    number = readNumber(int(address))
    print ('Arduino: Hey RPI, I received a digit ', number)
