from usb_iss import UsbIss, defs
from bitstring import BitArray
import numpy as np

# Configure I2C mode
iss = UsbIss()
iss.open("COMX") #Enter your COM port number
iss.setup_i2c()

temp1 = iss.i2c.read(0xA0, 0x36, 1)
first_byte = '{:08b}'.format(temp1[0])
version = (BitArray(bin=(first_byte))).int
version = hex(version)
print('Current FW Version = ', version)

temp1 = iss.i2c.read(0xA0, 0xA8, 4)
first_byte = '{:08b}'.format(temp1[3])
second_byte = '{:08b}'.format(temp1[2])
third_byte = '{:08b}'.format(temp1[1])
fourth_byte = '{:08b}'.format(temp1[0])
version = (BitArray(bin=(first_byte + second_byte + third_byte + fourth_byte))).int
version = hex(version)
print('TEST_FEE_CRC 0xA8 = ', version)

temp1 = iss.i2c.read(0xA0, 0x38, 2)
first_byte = '{:08b}'.format(temp1[1])
second_byte = '{:08b}'.format(temp1[0])
version = (BitArray(bin=(first_byte + second_byte))).int
version = hex(version)
print('STAT_FW_CRC 0x38 = ', version)


temp1 = iss.i2c.read(0xA0, 0x34, 1)
first_byte = '{:08b}'.format(temp1[0])
version = (BitArray(bin=(first_byte))).int
version = hex(version)
print('STAT_FAULT_SYSB 0x34 = ', version)
