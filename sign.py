#!/usr/bin/env python2

from cryptography.hazmat.backends.openssl import backend
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms
from struct import pack
from os import stat
from sys import argv, exit

if len(argv) != 3:
  print 'Usage: sign.py <input file> <output file>'
  exit(0)

fi=open(argv[1], 'rb')
a=pack('<LLQ',0,5,stat(argv[1]).st_size)+fi.read()
fi.close()
c=cmac.CMAC(algorithms.AES(pack('QQ',0,0)), backend=backend)
c.update(a)
d=c.finalize()
e='GSHV'+'\00\00\00\00'+d+bytes(bytearray(360))+a
fo=open(argv[2],'wb')
fo.write(e)
fo.close()

