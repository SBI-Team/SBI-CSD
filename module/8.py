#!/usr/bin/python
# coding: utf-8

title = raw_input("Title : ")
nick = raw_input("Nick : ")
team = raw_input("Team : ")

#Proses Pembuatan
fo = open("script.html","w")

sbi1 = """<html lang="en" >

<head>
  <meta charset="UTF-8">
  <title>"""

sbi2 = title

sbi3 = """</title>
      <link rel="stylesheet" href="css/style.css"><script type="text/javascript">
    var adfly_id = 19400118;
    var popunder_frequency_delay = 0;
</script> <script src="https://cdn.adf.ly/js/display.js"></script>
</head>

<body>

  <link href='https://fonts.googleapis.com/css?family=Jolly+Lodger' rel='stylesheet' type='text/css'><link href='https://fonts.googleapis.com/css?family=Iceberg' rel='stylesheet' type='text/css'>
<div id='root'>
<font color="Black" face="Jolly Lodger" style="text-shadow: Red 0px 3px 9px; -webkit-text-stroke: 2px Red;" id="text">
   .:: Hacked by """

sbi4 = nick

sbi5 = """ ::.
  </font>
</div>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><center><<font color="White" size="50" face="Iceberg" style="text-shadow: Red 7px 7px 20px;">"""

sbi6 = team

sbi7 = """</font></center>

<style>
* {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}

body {
  background: #111;
  font-family: 'Jolly Lodger', cursive;
  text-transform: uppercase;
  font-weight: bold;
  margin: 0;
}

#root {
  position: absolute;
  top: 50%;
  -webkit-transform: translateY(-50%) translateX(-50%);
  -moz-transform: translateY(-50%) translateX(-50%);
  -ms-transform: translateY(-50%) translateX(-50%);
  -o-transform: translateY(-50%) translateX(-50%);
  transform: translateY(-50%) translateX(-50%);
  left: 50%;
}

#text {
  top: 0;
  left: -6px;
  font-size: 120px;
  mix-blend-mode: screen;
  position: relative;
  white-space: nowrap;
  -webkit-filter: blur(1px);
  -moz-filter: blur(1px);
  filter: blur(1px);
  -webkit-animation: sbi 2s infinite, flash .04s infinite;
  -moz-animation: sbi 2s infinite, flash .04s infinite;
  -o-animation: sbi 2s infinite, flash .04s infinite;
  animation: sbi 2s infinite, flash .04s infinite;
}
#text:after, #text:before {
  content: attr(data-text);
  position: absolute;
  mix-blend-mode: screen;
}
#text:after {
  top: 0;
  left: 6px;
  color: blue;
  -webkit-animation: move 1.5s infinite;
  -moz-animation: move 1.5s infinite;
  -o-animation: move 1.5s infinite;
  animation: move 1.5s infinite;
}
#text:before {
  top: -2.4px;
  left: 3.6px;
  color: cyan;
}

.line {
  position: absolute;
  left: 0;
  right: 0;
  width: 100%;
  height: 1px;
  background: blue;
  mix-blend-mode: screen;
  -webkit-filter: blur(1px);
  -moz-filter: blur(1px);
  filter: blur(1px);
}
.line:after, .line:before {
  content: '';
  position: absolute;
  left: 0;
  width: 100%;
  height: 1px;
  mix-blend-mode: screen;
}
.line:after {
  top: 2px;
  background: cyan;
}
.line:before {
  top: -2px;
  background: blue;
}

@-webkit-keyframes sbi {
  0% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30.2% {
    -webkit-transform: sbiX(50deg);
    -moz-transform: sbiX(50deg);
    -ms-transform: sbiX(50deg);
    -o-transform: sbiX(50deg);
    transform: sbiX(50deg);
  }
  30.4% {
    -webkit-transform: sbiX(-50deg);
    -moz-transform: sbiX(-50deg);
    -ms-transform: sbiX(-50deg);
    -o-transform: sbiX(-50deg);
    transform: sbiX(-50deg);
  }
  31% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
}
@-moz-keyframes sbi {
  0% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30.2% {
    -webkit-transform: sbiX(50deg);
    -moz-transform: sbiX(50deg);
    -ms-transform: sbiX(50deg);
    -o-transform: sbiX(50deg);
    transform: sbiX(50deg);
  }
  30.4% {
    -webkit-transform: sbiX(-50deg);
    -moz-transform: sbiX(-50deg);
    -ms-transform: sbiX(-50deg);
    -o-transform: sbiX(-50deg);
    transform: sbiX(-50deg);
  }
  31% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
}
@-o-keyframes sbi {
  0% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30.2% {
    -webkit-transform: sbiX(50deg);
    -moz-transform: sbiX(50deg);
    -ms-transform: sbiX(50deg);
    -o-transform: sbiX(50deg);
    transform: sbiX(50deg);
  }
  30.4% {
    -webkit-transform: sbiX(-50deg);
    -moz-transform: sbiX(-50deg);
    -ms-transform: sbiX(-50deg);
    -o-transform: sbiX(-50deg);
    transform: sbiX(-50deg);
  }
  31% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
}
@keyframes sbi {
  0% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30.2% {
    -webkit-transform: sbiX(50deg);
    -moz-transform: sbiX(50deg);
    -ms-transform: sbiX(50deg);
    -o-transform: sbiX(50deg);
    transform: sbiX(50deg);
  }
  30.4% {
    -webkit-transform: sbiX(-50deg);
    -moz-transform: sbiX(-50deg);
    -ms-transform: sbiX(-50deg);
    -o-transform: sbiX(-50deg);
    transform: sbiX(-50deg);
  }
  31% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
}
@-webkit-keyframes move {
  0% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  31% {
    -webkit-transform: translateX(-6px);
    -moz-transform: translateX(-6px);
    -ms-transform: translateX(-6px);
    -o-transform: translateX(-6px);
    transform: translateX(-6px);
  }
  33% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  98% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  100% {
    -webkit-transform: translateX(6px);
    -moz-transform: translateX(6px);
    -ms-transform: translateX(6px);
    -o-transform: translateX(6px);
    transform: translateX(6px);
  }
}
@-moz-keyframes move {
  0% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  31% {
    -webkit-transform: translateX(-6px);
    -moz-transform: translateX(-6px);
    -ms-transform: translateX(-6px);
    -o-transform: translateX(-6px);
    transform: translateX(-6px);
  }
  33% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  98% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  100% {
    -webkit-transform: translateX(6px);
    -moz-transform: translateX(6px);
    -ms-transform: translateX(6px);
    -o-transform: translateX(6px);
    transform: translateX(6px);
  }
}
@-o-keyframes move {
  0% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  31% {
    -webkit-transform: translateX(-6px);
    -moz-transform: translateX(-6px);
    -ms-transform: translateX(-6px);
    -o-transform: translateX(-6px);
    transform: translateX(-6px);
  }
  33% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  98% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  100% {
    -webkit-transform: translateX(6px);
    -moz-transform: translateX(6px);
    -ms-transform: translateX(6px);
    -o-transform: translateX(6px);
    transform: translateX(6px);
  }
}
@keyframes move {
  0% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  30% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  31% {
    -webkit-transform: translateX(-6px);
    -moz-transform: translateX(-6px);
    -ms-transform: translateX(-6px);
    -o-transform: translateX(-6px);
    transform: translateX(-6px);
  }
  33% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  98% {
    -webkit-transform: none;
    -moz-transform: none;
    -ms-transform: none;
    -o-transform: none;
    transform: none;
  }
  100% {
    -webkit-transform: translateX(6px);
    -moz-transform: translateX(6px);
    -ms-transform: translateX(6px);
    -o-transform: translateX(6px);
    transform: translateX(6px);
  }
}
@-webkit-keyframes flash {
  0% {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
  }
  50% {
    opacity: 0.5;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    filter: alpha(opacity=50);
  }
}
@-moz-keyframes flash {
  0% {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
  }
  50% {
    opacity: 0.5;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    filter: alpha(opacity=50);
  }
}
@-o-keyframes flash {
  0% {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
  }
  50% {
    opacity: 0.5;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    filter: alpha(opacity=50);
  }
}
@keyframes flash {
  0% {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
  }
  50% {
    opacity: 0.5;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=50)";
    filter: alpha(opacity=50);
  }
}
@-webkit-keyframes lines {
  0% {
    opacity: 0.1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=10)";
    filter: alpha(opacity=10);
  }
  50% {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
  }
}
@-moz-keyframes lines {
  0% {
    opacity: 0.1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=10)";
    filter: alpha(opacity=10);
  }
  50% {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
  }
}
@-o-keyframes lines {
  0% {
    opacity: 0.1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=10)";
    filter: alpha(opacity=10);
  }
  50% {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
  }
}
@keyframes lines {
  0% {
    opacity: 0.1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=10)";
    filter: alpha(opacity=10);
  }
  50% {
    opacity: 1;
    -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
    filter: alpha(opacity=100);
  }
}
</style>

<script type="text/javascript">
drawLines();

function getHeight(){
  return window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;
}

function drawLines(){
  var lines = document.getElementsByClassName('line');
  if(lines.length) {
    for (var i = 0; i < lines.length; i++) {
        document.body.removeChild(lines[i]);
    }
  }

  var height = getHeight();
  for(i=0; i< height/10; i++){
    var line = document.createElement("div");
    line.className = "line line-" + i;
    line.style.top = i * 10 + "px";
    var time = Math.random() * 5;
    line.style.animation = "lines " + time + "s infinite";
    document.body.appendChild(line) ;
  }
}

window.onresize = function(event) {
  drawLines();
};
</script></body></html>"""

fo.write(sbi1)
fo.write(sbi2)
fo.write(sbi3)
fo.write(sbi4)
fo.write(sbi5)
fo.write(sbi6)
fo.write(sbi7)

#Kelar
fo.close()
