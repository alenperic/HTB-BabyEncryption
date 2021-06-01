#Alen's code
import string
import binascii
import struct


f = open('./msg.enc','r')
WR = f.read()
bytes = bytearray.fromhex(WR)
print(bytes)

struct.unpack(native, bytes)

def decryption(fart):
	dt = ''
	for char in fart:
		dt.append((127 / char -18) * 256)
	
	
dt = decryption(bytes)
print(dt)
s = open('./msg.dec','w')
s.write(dt.str)
f.close()
s.close()