#!/usr/bin/python
# coding: utf-8

title = raw_input("Title : ")
titlem = raw_input("Title [Bentuk Ketikkan Pertama] : ")
titlem2 = raw_input("Title [Bentuk Ketikkan Kedua] : ")
icon = raw_input("Gambar Icon [URL] : ")
nick = raw_input("Nick : ")
linkgmbr = raw_input("Gambar Tengah [URL] : ")
team = raw_input("Team : ")
sebab = raw_input("Sebab Situs Kena Deface [marquee] : ")
print "Warna Textnya [ex : cyan / Pakai Code Warna]"
colorm = raw_input("Masukkan : ")
print "Pesan [Pakai <br> Untuk Menggaanti Baris]"
pesan = raw_input("Masukkan : ")
print "Warna Textnya [ex : Red / Pakai Code Warna]"
colorp = raw_input("Masukkan : ")
musik = raw_input("Musik [URL] : ")

#Proses Pembuatan
fo = open("script.html","w")

sbi1 = """<html><head><title>"""

sbi2 = title

sbi3 = """</title><script type="text/javascript">
    var adfly_id = 19400118;
    var popunder_frequency_delay = 0;
</script><script src="https://cdn.adf.ly/js/display.js">
<link rel="shorcut icon" href=" """

sbi4 = icon

sbi5 = """ "><script type='text/javascript'>
//<![CDATA[
msg = "]>"""

sbi6 = titlem2

sbi7 = """ ";
msg = "]>"""

sbi8 = titlem


sbi9 = """ " + msg;pos = 0;
function scrollMSG() {
document.title = (pos, msg.length) + msg.substring(0, pos); pos++;
if (pos > msg.length) pos = 0
window.setTimeout("scrollMSG()",80);
}
scrollMSG();
//]]></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css">
<link href="https://fonts.googleapis.com/css?family=Jolly+Lodger" rel="stylesheet" type="text/css" />
<br><iframe width="0%" height="0" scrolling="no" frameborder="no" allow="autoplay" src=" """

sbi10 = musik

sbi11 = """ "></iframe>
<style type="text/css">
@import url(http://fonts.googleapis.com/css?family=Iceland);
@import url(http://fonts.googleapis.com/css?family=Josefin+Slab);
body { background: #254A00; color: brown; font-family :'Iceland'; background-color: #000000; background-size: 100%; background-repeat:no-repeat; background-attachment: fixed; background-size: cover; background-position:center; }

</style></head><body><div style="position: fixed; top: 75px; left: -225px; width: 600px; padding: 10px; font-size: 24px; text-align: center; color: red; font-family: 'trebuchet ms', verdana, arial, sans-serif;transform: rotate(-45deg);transform-origin: 50% 0px;-o-transform: rotate(-45deg); -o-transform-origin: 50% 0px;-moz-transform: rotate(-45deg); -moz-transform-origin: 50% 0px; -webkit-transform: rotate(-45deg); -webkit-transform-origin: 50% 0px; background-color: Transparent; border: 1px solid rgb(170, 170, 170); z-index: 9999; opacity: 0.5;"><a style="text-decoration:none;color:#58FAF4;">"""

sbi12 = nick

sbi13 = """</a></div>
<center>
<font style="-webkit-text-stroke: 1px white;" size="20" color="blue" face="Jolly Lodger"  >"""

sbi14 = nick

sbi15 = """</font>
<br>
        <br>
<center><img src=" """

sbi16 = linkgmbr

sbi17 = """ "</center><br>
<br><center>

        <br><center>
<font style="-webkit-text-stroke: 1px red;" size="20" color="white" face="Jolly Lodger"  >Team : """

sbi18 = team

sbi19 = """</font></center>

<font style="-webkit-text-stroke: 1px blue;" size="15" color="white" face="Iceland"> Sebab Situs TerDeface</font><marquee behavior="scroll" style="background:rgb(0,0,0); text-align:center; border-top: 1px solid white; border-bottom: 1px solid #58FAF4"><font style="-webkit-text-stroke: 1px """

sbi20 = colorm

sbi21 = """;" color="white" size="6" face="Iceland">"""

sbi22 = sebab

sbi23 = """</marquee>

<br>
</div>
</form><center><script language="JavaScript">
var text=" """

sbi24 = pesan

sbi25 = """ ";
var delay=100000000;
var currentChar=1;
var destination="[none]";
function type()
{
//if (document.all)
{
var dest=document.getElementById(destination);
if (dest)// && dest.innerHTML)
{
dest.innerHTML=text.substr(0, currentChar)+"<blink> </blink>";
currentChar++;
if (currentChar>text.length)
{
currentChar=1;
setTimeout("type()", 50000000);
}
else
{
setTimeout("type()", delay);
}
}
}
}
function startTyping(textParam, delayParam, destinationParam)
{
text=textParam;
delay=delayParam;
currentChar=1;
destination=destinationParam;
type();
}
</script>
<b><div id="B4n9Z4tt3r5" style="font: 41px arial; color:"""

sbi26 = colorp

sbi27 = """; background:#000000;border-radius:5px;margin: 0px;padding:5px 10px 5px 10px;"></div></b>
<script language="JavaScript">
javascript:startTyping(text, 50, "B4n9Z4tt3r5");
</script></center><br><center><font style="-webkit-text-stroke: 1px Yellow;" color="White" size="20" face="Jolly Lodger">Hacked By """

sbi28 = nick

sbi29 = """</font></center>
<script>alert('Hacked By """

sbi30 = nick

sbi31 = """');</script>
<script>alert('Team : """

sbi32 = team

sbi33 = """');</script></body></html>"""


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
fo.write(sbi14)
fo.write(sbi15)
fo.write(sbi16)
fo.write(sbi17)
fo.write(sbi18)
fo.write(sbi19)
fo.write(sbi20)
fo.write(sbi21)
fo.write(sbi22)
fo.write(sbi23)
fo.write(sbi24)
fo.write(sbi25)
fo.write(sbi26)
fo.write(sbi27)
fo.write(sbi28)
fo.write(sbi29)
fo.write(sbi30)
fo.write(sbi31)
fo.write(sbi32)
fo.write(sbi33)

#Selesai Pembuatan

fo.close()
