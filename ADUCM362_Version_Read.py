from usb_iss import UsbIss, defs
from bitstring import BitArray
import numpy as np

# Configure I2C mode
iss = UsbIss()
iss.open("COMXX") #Enter Your USB serial Com Port
iss.setup_i2c()

temp = iss.i2c.read(0xA0, 0x36, 2) #0xA0 is 7bit I2C address of device + writebit
first_byte = '{:08b}'.format(temp[1])
second_byte = '{:08b}'.format(temp[0])
version = (BitArray(bin=(first_byte + second_byte))).int
print('Version =', version)