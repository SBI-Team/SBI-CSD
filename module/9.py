#!/usr/bin/python
# coding: utf-8

title = raw_input("Title : ")
nick = raw_input("Nick : ")
gambar = raw_input("Gambar [URL] : ")
team = raw_input("Team : ")
thanks = raw_input("Thanks To : ")
pesan = raw_input("Message [ <br> Untuk Ganti Baris ] : ")

#Proses Pembuatan
fo = open("script.html","w")

sbi1 = """<html><head><title>"""

sbi2 = title

sbi3 = """</title>
<script type="text/javascript">
    var adfly_id = 19400118;
    var popunder_frequency_delay = 0;
</script> <script src="https://cdn.adf.ly/js/display.js"></script>
<style>
.error {
  text-align: center;
  font-family: 'null', serif;
  -webkit-animation: noise-3 1s linear infinite;
          animation: noise-3 1s linear infinite;
  overflow: default;
}


.info {
  text-align: center;
  width: 200px;
  height: 60px;
  margin: auto;
  position: absolute;
  top: 280px;
  bottom: 0;
  left: 20px;
  right: 0;
  -webkit-animation: noise-3 1s linear infinite;
          animation: noise-3 1s linear infinite;
}


.info:after {
  content: 'OWNED';
  font-family: OCR-A;
  font-size: 100px;
  text-align: center;
  width: 800px;
  margin: auto;
  position: absolute;
  top: 20px;
  bottom: 0;
  left: 40px;
  right: 0;
  opacity: 0;
  color: white;
  -webkit-animation: noise-1 .2s linear infinite;
          animation: noise-1 .2s linear infinite;
}

@-webkit-keyframes noise-1 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: -6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: 2px;}
}

@keyframes noise-1 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: -6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: 2px;}
}

@-webkit-keyframes noise-2 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: 6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: -2px;}
}

@keyframes noise-2 {
  0%, 20%, 40%, 60%, 70%, 90% {opacity: 0;}
  10% {opacity: .1;}
  50% {opacity: .5; left: 6px;}
  80% {opacity: .3;}
  100% {opacity: .6; left: -2px;}
}

@-webkit-keyframes noise {
  0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}    4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);}
  43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);}
}

@keyframes noise {
  0%, 3%, 5%, 42%, 44%, 100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}  
  4.3% {opacity: 1; -webkit-transform: scaleY(1.7); transform: scaleY(1.7);}
  43% {opacity: 1; -webkit-transform: scaleX(1.5); transform: scaleX(1.5);}
}

@-webkit-keyframes noise-3 {
  0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}
  4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);}
  43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate(60deg);}
}

@keyframes noise-3 {
  0%,3%,5%,42%,44%,100% {opacity: 1; -webkit-transform: scaleY(1); transform: scaleY(1);}
  4.3% {opacity: 1; -webkit-transform: scaleY(4); transform: scaleY(4);}
  43% {opacity: 1; -webkit-transform: scaleX(10) rotate(60deg); transform: scaleX(10) rotate(60deg);}
}

.wrap {
  top: 30%;
  left: 25%;

  height: 200px;

  margin-top: -100px;
  position: absolute;
}
code {
  color: white;
}
span.blue {
  color: #48beef;
}
span.comment {
  color: #7f8c8d;
}
span.orange {
  color: #f39c12;
}
span.green {
  color: #33cc33;
}

.viewFull {
  font-family:OCR-A;
  color:orange;
  text-decoration:;
}


}

 @media only screen and (min-height: 500px) {

.viewFull{
  display:none;
	}

}

</style><link href='https://fonts.googleapis.com/css?family=Jolly+Lodger' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Iceberg' rel='stylesheet' type='text/css'></head><body bgcolor="black">
<center><div class="error"><br><font color="White" face="Jolly Lodger" size="50px" style="-webkit-text-stroke: 1px Black; text-shadow: Red 0px 3px 9px; ">.:: Hacked By """

sbi4 = nick

sbi5 = """ ::.</font><br><br><img size="50px" src=" """

sbi6 = gambar

sbi7 = """ "/><br><br><font color="Black" style="-webkit-text-stroke: 1px White; text-shadow: Red 0px 3px 9px; " face="Jolly Lodger" size="9px">"""

sbi8 = team

sbi9 = """</font></div><br><font face="Jolly Lodger" color="Red" size="6px">Thanks To : </font><marquee behavior="alternate" scrollamount="5" size="6px" style="border:1px solid; color:white;text-shadow: Red 0px 3px 9px; " width="75%"><font size="5px">|| """

sbi10 = thanks

sbi11 = """ ||</font></marquee><br><br><div class="error"><font color="White" face="Jolly Lodger">Message : </font><br><font color="Red" face="Iceberg">"""

sbi12 = pesan

sbi13 = """</font></div><br><font color="#9E9E9E" face="Courier" size="1px"><<<</font><font color="White" face="Courier" size="1px"> &copy; 2k19 </font><font color="Red" face="Jolly Lodger" size="1px" style="text-shadow: White 0px 1px 2px;">ShaDoW BlooD InDoNeSiA</font><font color="#9E9E9E" face="Courier" size="1px"> >>></font></center></body></html>"""

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

#Kelar
fo.close()
