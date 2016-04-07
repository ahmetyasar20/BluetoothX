#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bluetooth import *
import sys

port = 0
sunucu=BluetoothSocket( RFCOMM )
sunucu.bind(("",port))
sunucu.listen(1)
print "%d portunu dinliyorum" % port


istemci,adres = sunucu.accept()
print "%s adresine baglanildi "% (adres)

data = istemci.recv(1024)
print "Istemciden alinan veri: [%s]" % data

istemci.close()
istemci.close()
