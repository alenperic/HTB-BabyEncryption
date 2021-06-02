# HTB_BabyEncryption

Solution to the Python reverse encryption script that is provided in the **Hack The Box: Challange: *BabyEncryption***
This script will translate and print the encrypted message, as well as store it in msg.dec

## **Code:**
```python
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
```
