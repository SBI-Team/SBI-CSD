#!/usr/bin/python
# coding: utf-8

title = raw_input("Title : ")
nick = raw_input("Nick : ")
musik = raw_input("Musik [URL] : ")
gambar = raw_input("Gambar [URL] : ")
pesan = raw_input("Pesan [Tanpa <br>/Enter] : ")
thanks = raw_input("Thanks To : ")
team = raw_input("Team : ")

fo = open("script.html","w")

sbi1 = """<html><head><title>"""

sbi2 = title

sbi3 = """</title>
<script>
alert('Syukur Itu Kunci Bahagia');
alert('Mungkin terlihat sepele seperti oksigen yang kita hirup, Air yang kita minum');
alert('Apapun yang terjadi dalam hidupmu jangan lupa untuk bersyukur');
</script>
<style type="text/css">
@import url(https://fonts.googleapis.com/css?family=Iceberg);
@import url(https://fonts.googleapis.com/css?family=Sedgwick+Ave+Display);
@import url(https://fonts.googleapis.com/css?family=Jolly+Lodger);
@import url(https://fonts.googleapis.com/css?family=Margarine|Trade+Winds);
}
.go {
font-size : 50px;
}
.yes1 {
border: 5px White double;
}
.yes2 {opacity:0.5;-webkit-transition:all 250ms ease;-moz-transition:all 250ms ease;-o-transition:all 250ms ease;transition:all 250ms ease;margin-top:-10px;
}

.yes2:hover{opacity:1.0}
h1 {
  text-align: center;
  color: Black;
  font-size: 3em;
  letter-spacing: 1px;
  font-family: 'Sedgwick Ave Display';
  font-weight: 400;
  /*Create overlap*/

  margin: 0;
  line-height: 0;
  /*Animation*/

  -webkit-animation: glitch1 2.5s infinite;

          animation: glitch1 2.5s infinite;
}

h1:nth-child(2) {
  color: White;
  -webkit-animation: glitch2 2.5s infinite;
          animation: glitch2 2.5s infinite;
}

h1:nth-child(3) {
  color: White;
  -webkit-animation: glitch3 2.5s infinite;
          animation: glitch3 2.5s infinite;
}
/*Keyframes*/

@-webkit-keyframes glitch1 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  7% {
    -webkit-transform: skew(-0.5deg, -0.9deg);
            transform: skew(-0.5deg, -0.9deg);
    opacity: 0.75;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  30% {
    -webkit-transform: skew(0.8deg, -0.1deg);
            transform: skew(0.8deg, -0.1deg);
    opacity: 0.75;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  55% {
    -webkit-transform: skew(-1deg, 0.2deg);
            transform: skew(-1deg, 0.2deg);
    opacity: 0.75;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  75% {
    -webkit-transform: skew(0.4deg, 1deg);
            transform: skew(0.4deg, 1deg);
    opacity: 0.75;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
}

@keyframes glitch1 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  7% {
    -webkit-transform: skew(-0.5deg, -0.9deg);
            transform: skew(-0.5deg, -0.9deg);
    opacity: 0.75;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  30% {
    -webkit-transform: skew(0.8deg, -0.1deg);
            transform: skew(0.8deg, -0.1deg);
    opacity: 0.75;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  55% {
    -webkit-transform: skew(-1deg, 0.2deg);
            transform: skew(-1deg, 0.2deg);
    opacity: 0.75;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  75% {
    -webkit-transform: skew(0.4deg, 1deg);
            transform: skew(0.4deg, 1deg);
    opacity: 0.75;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 1;
  }
}

@-webkit-keyframes glitch2 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(-2px, -3px);
            transform: translate(-2px, -3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(-5px, -2px);
            transform: translate(-5px, -2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(-5px, -1px);
            transform: translate(-5px, -1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(-2px, -6px);
            transform: translate(-2px, -6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}

@keyframes glitch2 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(-2px, -3px);
            transform: translate(-2px, -3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(-5px, -2px);
            transform: translate(-5px, -2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(-5px, -1px);
            transform: translate(-5px, -1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(-2px, -6px);
            transform: translate(-2px, -6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
mm
@-webkit-keyframes glitch3 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(2px, 3px);
            transform: translate(2px, 3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(5px, 2px);
            transform: translate(5px, 2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(5px, 1px);
            transform: translate(5px, 1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(2px, 6px);
            transform: translate(2px, 6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}

@keyframes glitch3 {
  0% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  7% {
    -webkit-transform: translate(2px, 3px);
            transform: translate(2px, 3px);
    opacity: 0.5;
  }
  10% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  27% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  30% {
    -webkit-transform: translate(5px, 2px);
            transform: translate(5px, 2px);
    opacity: 0.5;
  }
  35% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  52% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  55% {
    -webkit-transform: translate(5px, 1px);
            transform: translate(5px, 1px);
    opacity: 0.5;
  }
  50% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  72% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  75% {
    -webkit-transform: translate(2px, 6px);
            transform: translate(2px, 6px);
    opacity: 0.5;
  }
  80% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
  100% {
    -webkit-transform: none;
            transform: none;
    opacity: 0.25;
  }
}
</style><script type="text/javascript">
    var adfly_id = 19400118;
    var popunder_frequency_delay = 0;
</script>
<script src="https://cdn.adf.ly/js/display.js"></script></head><body bgcolor="Black"><script type="text/javascript" src="http://htmlfreecodes.com/codes/rain.js"></script><center><br><h1 class="go" style="font-style : italic; text-shadow: Red 0px 2px 6px; -webkit-text-stroke: 1px Red;" face="Sedgwick Ave Display" color="Black">::: Hacked By """

sbi4 = nick

sbi5 = """ :::</h1><br><br><img src="http://rs1149.pbsrc.com/albums/o587/GxDDP/bendera-rosulullah_zpsxbagucbk.png?w=480&h=480&fit=clip" class="yes1" width="380"/><font color="Black">‌    </font><img src="http://rs1149.pbsrc.com/albums/o587/GxDDP/20181226_111945_zpsu0f39ezc.jpg?w=480&h=480&fit=clip" class="yes1" width="380"/><br><br><audio autoplay="autoplay" controls="controls"  width="500px" height="250px"><source src=" """

sbi6 = musik

sbi7 = """ "></audio><br><marquee behavior="scroll" direction="left" scrollamount="100" scrolldelay="90" width="100%"><font color="white">____________________________________________________________________________________</font></marquee><font class="go" face="Jolly Lodger" style="-webkit-text-stroke: 1px #58FAF4;" color="Black">Muslim Indonesia</font><marquee behavior="scroll" direction="right" scrollamount="100" scrolldelay="90" width="100%"><font color="white">____________________________________________________________________________________</font></marquee><br><br><img src=" """

sbi8 = gambar

sbi9 = """ " class="yes2" width="400"/><br><font size="3px" face="Iceberg" color="Red">Semua yang Ada di Dunia ini Akan Lenyap</fonr><br><font size="3px" color="Yellow">Jangan Bergantung Kepada Manusia</font><br><font size="3px" color="White">Bergantunglah Kepada Allah</font><br><font size="3px" color="Blue">Dengan Begitu Hidupmu Akan Senang dan Bahagia</font><br><br><input type="button" value="Message" onclick="alert('"""

sbi10 = pesan

sbi11 = """');" style="font-size:3,200em;background:Blue;color:white;"></a><br><font color="White" size="3px">Thanks To : </font><marquee behavior="alternate" scrollamount="5" style="border:1px solid; color:white;" width="75%"><font>[$]==>"""

sbi12 = thanks

sbi13 = """<==[$]</font></marquee><br><font color="Blue" size="3px">Team : </font><font color="White" size="3px" face="Jolly Lodger" style="text-shadow: Red 0px 2px 6px;">"""

sbi14 = team

sbi15 = """</font></center></body></html>"""

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

fo.close()
