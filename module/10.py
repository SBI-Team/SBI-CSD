#!/usr/bin/python
# coding: utf-8

title = raw_input("Title : ")
icon = raw_input("Icon : ")
gambar = raw_input("Gambar [URL] : ")
nick = raw_input("Nick : ")
pesan = raw_input("Message [ <br> Untuk Ganti Baris ] : ")
thx = raw_input("Thanks To : ")

fo = open("script.html","w")

sbi1 = """<html><head><title>"""

sbi2 = title

sbi3 = """</title></head><link href='http://fonts.googleapis.com/css?family=Iceland' rel='stylesheet' type='text/css'><link href='http://fonts.googleapis.com/css?family=Audiowide' rel='stylesheet' type='text/css'><link href='https://fonts.googleapis.com/css?family=Iceberg' rel='stylesheet' type='text/css'><link href=" """

sbi4 = icon

sbi5 = """ " rel="shortcut icon" /><body dir="ltr" alink="#0033FF" background="" bgcolor="#000000" link="grey" text="grey" vlink="#FF0000"><font class="hk2" style="text-shadow: 1px -1px 8px;"><br><br><br><br><center><h2><table><tr><td><img src=" """

sbi6 = gambar

sbi7 = """ " widht="350" height="350"></td><td><font face="Iceberg" size="6" color="Red">-=[ Hacked by """

sbi8 = nick

sbi9 = """ ]=-<center></center></h2><h6></font><span style="syntax"><font face="Audiowide" size="3" color="black" style="-webkit-text-stroke: 1px White; text-shadow: Red 0px 3px 9px; ">Message :</font><br><font face="Iceland" size="5" color="black" style="-webkit-text-stroke: 1px White; text-shadow: Red 0px 3px 9px; ">"""

sbi10 = pesan

sbi11 = """</font></h6><br></td></tr></table><marquee onmouseout=this.start() onmouseover=this.stop()  scrolldelay='10'><font color="White" face="Audiowide" size="3" style="-webkit-text-stroke: 1px Black; text-shadow: Red 0px 3px 9px; ">"""

sbi12 = thx

sbi13 = """</font></marquee></html>"""

fo.write(sbi1)
fo.write(sbi2)
fo.write(sbi3)
fo.write(sbi4)
fo.write(sbi5)
fo.write(sbi6)
fo.write(sbi7)
fo.write(sbi8)
fo.write(sbi9)
fo.write(sbi10)
fo.write(sbi11)
fo.write(sbi12)
fo.write(sbi13)

fo.close()
