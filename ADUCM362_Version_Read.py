from usb_iss import UsbIss, defs
from bitstring import BitArray
import sys

# Configure I2C mode
iss = UsbIss()
iss.open("COMX") #Enter your COM port number
iss.setup_i2c()

temp1 = iss.i2c.read(0xA0, 0x36, 1)
first_byte = '{:08b}'.format(temp1[0])
version = (BitArray(bin=(first_byte))).int
version = hex(version)
print('Current FW Version = ', version)
if version == "-1":
    print("Chip not programmed, try reading multiple times")

else:
    print("Verify the programmed version matching the current FW version")


temp1 = iss.i2c.read(0xA0, 0xA8, 4)
first_byte = '{:08b}'.format(temp1[3])
second_byte = '{:08b}'.format(temp1[2])
third_byte = '{:08b}'.format(temp1[1])
fourth_byte = '{:08b}'.format(temp1[0])
version = (BitArray(bin=(first_byte + second_byte + third_byte + fourth_byte))).int
version = hex(version)
print('TEST_FEE_CRC 0xA8 = ', version)
#This command is used to provide the reference CRC calculated by the on-chip hardware.
# In a post-compile step, this value is inserted into the object file programmed into the flash memory to provide the
# reference against which future start-up CRC calculations are compared. In the event of a CRC failure, this register
# will hold the failing value.
if version == "0x5bd0ee2d":
    print("CRC of program code, Passed")
else:
    print("CRC of program code, Failed!")


temp1 = iss.i2c.read(0xA0, 0x38, 2)
first_byte = '{:08b}'.format(temp1[1])
second_byte = '{:08b}'.format(temp1[0])
version = (BitArray(bin=(first_byte + second_byte))).int
version = hex(version)
print('STAT_FW_CRC 0x38 = ', version)
#This register indicates if the firmware CRC was valid or not. The CRC is calculated automatically after reset.
# An incorrect CRC result will cause the FLT_FW_CRC bit in the STAT_FAULT_SYSB register to be set.
# This register indicates 0x5AA5 if the internal CRC check is valid. It indicates 0xFFFF if the CRC check is invalid.
if version == "0x5aa5":
    print("Firmware CRC calculated after reset, Passed")
else:
    print("Firmware CRC calculated after reset, Failed!")


temp1 = iss.i2c.read(0xA0, 0x34, 1)
first_byte = '{:08b}'.format(temp1[0])
version = (BitArray(bin=(first_byte))).int
version = hex(version)
print('STAT_FAULT_SYSB 0x34 = ', version)
# Bit1 of 0x34 indicate the IC trim CRC is invalid or not
if version == "0x0":
    print("Status of CRC verification, Passed")
else:
    print("Status of CRC verification, Failed")
