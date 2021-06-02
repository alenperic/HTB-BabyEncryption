#!/usr/bin/env python3
#Alen's code
import string

f = open('./msg.enc','r')
WR = f.read()
MSG = bytearray.fromhex(WR)

def decryption(msg):
    pt = []
    for char in msg:
        char = char - 18
        char = 179 * char % 256
        pt.append(char)
    return bytes(pt)

pt = decryption(MSG)
print(pt)

s = open('./msg.dec','w')
s.write(str(pt))
f.close()
s.close()
