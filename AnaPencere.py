#!/usr/bin/env python

from Tkinter import *
        
##############################################################
#Pencerenin nasıl görüneceğini belirliyoruz.                 #
#resizable = kullanıcı boyutlandıramayacak şekilde ayarlandı #
#pady, padx = her kontrol için 10,10 olarak padding ayarlandı#
#bg = butonların backgroundu beyaz yapıldı.                  #
##############################################################
pencere = Tk()
pencere.title("Bilgisayar-Bluetooth Haberleşme Projesi")
pencere.resizable(width=FALSE, height=FALSE)

AcKapaTusu = Checkbutton(text="Bluetooth Aç/Kapat")
AcKapaTusu.pack(pady=10, padx=10)

cihazListesi = Listbox()
cihazListesi.pack(side=LEFT, pady=10, padx=10)

cihazBul = Button(text="Etraftaki Cihazları Bul", bg="white")
cihazBul.config(width=20, height=1)
cihazBul.pack(pady=10, padx=10)

seriPortaBaglan = Button(text="Seri Portla Haberleşme", bg="white")
seriPortaBaglan.config(width=20, height=1)
seriPortaBaglan.pack(pady=10, padx=10)

paralelPortaBaglan = Button(text="Paralel Portla Haberleşme", bg="white")
paralelPortaBaglan.config(width=20, height=1)
paralelPortaBaglan.pack(pady=10, padx=10)

bosPortBul = Button(text="Boştaki Portları Bul", bg="white")
bosPortBul.config(width=20, height=1)
bosPortBul.pack(pady=10, padx=10)

dosyaGonder = Button(text="Dosya Gönder", bg="white")
dosyaGonder.config(width=20, height=1)
dosyaGonder.pack(pady=10, padx=10)

mainloop()


