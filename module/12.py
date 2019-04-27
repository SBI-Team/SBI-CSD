#!/usr/bin/python
# coding: utf-8

title = raw_input("Title : ")
nick = raw_input("Nick : ")
icon = raw_input("Icon [URL] : ")
gambar = raw_input("Gambar [URL] : ")
team = raw_input("Team : ")
thx = raw_input("Thanks To : ")

fo = open("script.html","w")

sbi1 = """<!DOCTYPE html>
 <html>
 <head><script type="text/javascript">     var adfly_id = 19400118;     var popunder_frequency_delay = 0; </script> <script src="https://cdn.adf.ly/js/display.js"></script>
	 <title>"""

sbi2 = title

sbi3 = """</title>
	 <meta charset="UTF-8"/>
	 <link rel="stylesheet" href="" type="text/css"/>
 </head>
	 <body>

	 </body>
 </html>
 <html><head>

<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">

<title>-----Defaced by """

sbi4 = nick

sbi5 = """ -----.</title>

<link rel="SHORTCUT ICON" href=" """

sbi6 = icon

sbi7 = """ "></head><body bgcolor=black><center>


<style type="text/css">body {cursor:url(""),default}</style>


<link rel="icon" type="image/gif" href=" """

sbi8 = icon

sbi9 = """ ">


<div align="center"><table border="0" width="70%"><tr><td>


<h1><font face="Cooper Black"><center><SCRIPT>


farbbibliothek = new Array();


farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100");


farbbibliothek[1] = new Array("#FF0000","#FFFFFF","#FFFFFF","#FF0000");


farbbibliothek[2] = new Array("#FFFFFF","#FF0000","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF");


farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040");


farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000");


farbbibliothek[5] = new Array("#FF0000","#FF0000","#FF0000","#FFFFFF","#FFFFFF","#FFFFFF");


farbbibliothek[6] = new Array("#FF0000","#FDF5E6");


farben = farbbibliothek[4];


function farbschrift()


{


for(var i=0 ; i<Buchstabe.length; i++)


{


document.all["a"+i].style.color=farben[i];


}


farbverlauf();


}


function string2array(text)


{


Buchstabe = new Array();


while(farben.length<text.length)


{


farben = farben.concat(farben);


}


k=0;


while(k<=text.length)


{


Buchstabe[k] = text.charAt(k);


k++;


}


}


function divserzeugen()


{


for(var i=0 ; i<Buchstabe.length; i++)


{


document.write("<span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span>");


}


farbschrift();


}


var a=1;


function farbverlauf()


{


for(var i=0 ; i<farben.length; i++)


{


farben[i-1]=farben[i];


}


farben[farben.length-1]=farben[-1];


setTimeout("farbschrift()",30);


}


//


var farbsatz=1;


function farbtauscher()


{


farben = farbbibliothek[farbsatz];


while(farben.length<text.length)


{


farben = farben.concat(farben);


}


farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001));


}


setInterval("farbtauscher()",5000);


text ="---Hacked By """

sbi10 = nick

sbi11 = """---.";//h


string2array(text);


divserzeugen();


//document.write(text);


</SCRIPT></center></h1></font>


<center><img src=" """

sbi12 = gambar

sbi13 = """ "


<font color="green" face="calibri" size="14">


<script language="JavaScript">

/*

An object-oriented Typing Text script, to allow for multiple instances.

A script that causes any text inside any text element to be "typed out", one letter at a time. Note that any HTML tags will not be included in the typed output, to prevent them from causing problems. Tested in Firefox v1.5.0.1, Opera v8.52, Konqueror v3.5.1, and IE v6.

Browsers that do not support this script will simply see the text fully displayed from the start, including any HTML tags.


Functions defined:

  TypingText(element, [interval = 100,] [cursor = "",] [finishedCallback = function(){return}]):

    Create a new TypingText object around the given element.  Optionally

    specify a delay between characters of interval milliseconds.

    cursor allows users to specify some HTML to be appended to the end of

    the string whilst typing.  Optionally, can also be a function which

    accepts the current text as an argument.  This allows the user to

    create a "dynamic cursor" which changes depending on the latest character

    or the current length of the string.

    finishedCallback allows advanced scripters to supply a function

    to be executed on finishing.  The function must accept no arguments.


  TypingText.run():

    Run the effect.


  static TypingText.runAll():

    Run all TypingText-enabled objects on the page.

*/


TypingText = function(element, interval, cursor, finishedCallback) {

  if((typeof document.getElementById == "undefined") || (typeof element.innerHTML == "undefined")) {

    this.running = true; // Never run.

    return;

  }

  this.element = element;

  this.finishedCallback = (finishedCallback ? finishedCallback : function() { return; });

  this.interval = (typeof interval == "undefined" ? 20 : interval);

  this.origText = this.element.innerHTML;

  this.unparsedOrigText = this.origText;

  this.cursor = (cursor ? cursor : "");

  this.currentText = "";

  this.currentChar = 0;

  this.element.typingText = this;

  if(this.element.id == "") this.element.id = "typingtext" + TypingText.currentIndex++;

  TypingText.all.push(this);

  this.running = false;

  this.inTag = false;

  this.tagBuffer = "";

  this.inHTMLEntity = false;

  this.HTMLEntityBuffer = "";

}

TypingText.all = new Array();

TypingText.currentIndex = 0;

TypingText.runAll = function() {

  for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run();

}

TypingText.prototype.run = function() {

  if(this.running) return;

  if(typeof this.origText == "undefined") {

    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval); // We haven't finished loading yet.  Have patience.

    return;

  }

  if(this.currentText == "") this.element.innerHTML = "";

//  this.origText = this.origText.replace(/<([^<])*>/, "");     // Strip HTML from text.

  if(this.currentChar < this.origText.length) {

    if(this.origText.charAt(this.currentChar) == "<" && !this.inTag) {

      this.tagBuffer = "<";

      this.inTag = true;

      this.currentChar++;

      this.run();

      return;

    } else if(this.origText.charAt(this.currentChar) == ">" && this.inTag) {

      this.tagBuffer += ">";

      this.inTag = false;

      this.currentText += this.tagBuffer;

      this.currentChar++;

      this.run();

      return;

    } else if(this.inTag) {

      this.tagBuffer += this.origText.charAt(this.currentChar);

      this.currentChar++;

      this.run();

      return;

    } else if(this.origText.charAt(this.currentChar) == "&" && !this.inHTMLEntity) {

      this.HTMLEntityBuffer = "&";

      this.inHTMLEntity = true;

      this.currentChar++;

      this.run();

      return;

    } else if(this.origText.charAt(this.currentChar) == ";" && this.inHTMLEntity) {

      this.HTMLEntityBuffer += ";";

      this.inHTMLEntity = false;

      this.currentText += this.HTMLEntityBuffer;

      this.currentChar++;

      this.run();

      return;

    } else if(this.inHTMLEntity) {

      this.HTMLEntityBuffer += this.origText.charAt(this.currentChar);

      this.currentChar++;

      this.run();

      return;

    } else {

      this.currentText += this.origText.charAt(this.currentChar);

    }

    this.element.innerHTML = this.currentText;

    this.element.innerHTML += (this.currentChar < this.origText.length - 1 ? (typeof this.cursor == "function" ? this.cursor(this.currentText) : this.cursor) : "");

    this.currentChar++;

    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);

  } else {

 this.currentText = "";

 this.currentChar = 0;

        this.running = false;

        this.finishedCallback();

  }

}

</script>

<style>

td{align: center; font-family: Bradley Hand ITC; font-size: 12pt; color: red}

a{align: center; font-family: Bradley Hand ITC; font-size: 12pt; color: red}


</style>

<div id="example1"></div>

<p id="example2">


<font face=calibri color=white size=3>

DEFACER : <font face=calibri color=green size=4>"""

sbi14 = nick

sbi15 = """<br> </font>

<font face=calibri color=white size=3>

TEAM : <font face=calibri color=green size=4>"""

sbi16 = team

sbi17 = """<br> </font>

<font face=calibri color=white size=3>

FROM : <font face=calibri color=green size=4>"""

sbi18 = team

sbi19 = """<br> </font>

<font face=calibri color=white size=3>

TO : <font face=calibri color=green size=4>All being hurt.<br></font>


<br>

<i><font face=calibri color=white size=4>

<font face=calibri color=green size-4>==========================================================<br>

Kami hadir karen orang yang kami sayang menyakiti kami------------------------------------------==<br>

Disaat orang yang kita sayang lebih menyayangi orang lain kami merasa sedih.--==<br>

Disaat orang yang kita suka lebih menyukai orang lain kita merasa luka dan duka.-----------------------==<br>

Dan disaat orang yang kita cintai lebih mencintai orang lain kita merasa tak berharga.----==<br>

Namun rasa sakit memang Sulit di tutupi,--------------------------------------------------------------==<br>

melihatnya bahagia lebih berharga dari pada cinta ini,--------------------------------------------------------==<br>

dan hati ini hanya dapat merasakan sakit hati yang sangat dalam tanpa dapat diungkapkan--------------==<br>

kini problem itu yang membuat kami melakukan tidakan ini untuk meluapkan emosi kami--------------------------==<br>

Pesan kami untuk orang yang menyakiti kami-------------------------------------------------------==<br>

" Jangan pernah menyia-nyiakan orang yang mencintai anda-----------------------------------------==<br>

   Karena belum tentu masih banyak orang yang mencintai anda dengan tulus----------------------==<br>

<font face=calibri color=green size-4>===========================================================<br>


<br>

<br>

<font face=calibri color=red size=5><b>

<marquee width=75%>"""

sbi20 = team

sbi21 = """ was here !</marquee></br></font>

<font face=calibri color=white size=4><b>

<marquee width=50%>Copyleft � 2019</marquee>

   

</p><script type="text/javascript">

//Define first typing example:

new TypingText(document.getElementById("example1"));

//Define second typing example (use "slashing" cursor at the end):

new TypingText(document.getElementById("example2"), 50, function(i){

var ar = new Array("_"," ","_","_"); return " " + ar[i.length %

ar.length]; });

//Type out examples:

TypingText.runAll();


</script>


<script language="JavaScript" type="text/javascript">


<!--

var rows=1; // must be an odd number

var speed=10; // lower is faster

var reveal=2; // between 0 and 2 only. The higher, the faster the word appears

var effectalign="default" //enter "center" to center it.


/***********************************************

* The Matrix Text Effect- by Richard Womersley (http://www.mf2fm.co.uk/rv)

* This notice must stay intact for use

* Visit http://www.dynamicdrive.com/ for full source code

***********************************************/


var w3c=document.getElementById && !window.opera;;

var ie45=document.all && !window.opera;

var ma_tab, matemp, ma_bod, ma_row, x, y, columns, ma_txt, ma_cho;

var m_coch=new Array();

var m_copo=new Array();

function matrix() {

if (!w3c && !ie45) return

var matrix=(w3c)?document.getElementById("matrix"):document.all["matrix"];

ma_txt=(w3c)?matrix.firstChild.nodeValue:matrix.innerHTML;

ma_txt=" "+ma_txt+" ";

columns=ma_txt.length;

if (w3c) {

while (matrix.childNodes.length) matrix.removeChild(matrix.childNodes[0]);

ma_tab=document.createElement("table");

ma_tab.setAttribute("border", 0);

ma_tab.setAttribute("align", effectalign);

ma_tab.style.backgroundColor="#000000";

ma_bod=document.createElement("tbody");

for (x=0; x<rows; x++) {

ma_row=document.createElement("tr");

for (y=0; y<columns; y++) {

matemp=document.createElement("td");

matemp.setAttribute("id", "Mx"+x+"y"+y);

matemp.className="matrix";

matemp.appendChild(document.createTextNode(String.fromCharCode(160)));

ma_row.appendChild(matemp);

}

ma_bod.appendChild(ma_row);

}

ma_tab.appendChild(ma_bod);

matrix.appendChild(ma_tab);

} else {

ma_tab='<ta'+'ble align="'+effectalign+'" border="0" style="background-color:#000000">';

for (var x=0; x<rows; x++) {

ma_tab+='<t'+'r>';

for (var y=0; y<columns; y++) {

ma_tab+='<t'+'d class="matrix" id="Mx'+x+'y'+y+'">&nbsp;</'+'td>';

}

ma_tab+='</'+'tr>';

}

ma_tab+='</'+'table>';

matrix.innerHTML=ma_tab;

}

ma_cho=ma_txt;

for (x=0; x<columns; x++) {

ma_cho+=String.fromCharCode(32+Math.floor(Math.random()*94));

m_copo[x]=0;

}

ma_bod=setInterval("mytricks()", speed);

}


function mytricks() {

x=0;

for (y=0; y<columns; y++) {

x=x+(m_copo[y]==100);

ma_row=m_copo[y]%100;

if (ma_row && m_copo[y]<100) {

if (ma_row<rows+1) {

if (w3c) {

matemp=document.getElementById("Mx"+(ma_row-1)+"y"+y);

matemp.firstChild.nodeValue=m_coch[y];

}

else {

matemp=document.all["Mx"+(ma_row-1)+"y"+y];

matemp.innerHTML=m_coch[y];

}

matemp.style.color="#33ff66";

matemp.style.fontWeight="bold";

}

if (ma_row>1 && ma_row<rows+2) {

matemp=(w3c)?document.getElementById("Mx"+(ma_row-2)+"y"+y):document.all["Mx"+(ma_row-2)+"y"+y];

matemp.style.fontWeight="normal";

matemp.style.color="#00ff00";

}

if (ma_row>2) {

matemp=(w3c)?document.getElementById("Mx"+(ma_row-3)+"y"+y):document.all["Mx"+(ma_row-3)+"y"+y];

matemp.style.color="#009900";

}

if (ma_row<Math.floor(rows/2)+1) m_copo[y]++;

else if (ma_row==Math.floor(rows/2)+1 && m_coch[y]==ma_txt.charAt(y)) zoomer(y);

else if (ma_row<rows+2) m_copo[y]++;

else if (m_copo[y]<100) m_copo[y]=0;

}

else if (Math.random()>0.9 && m_copo[y]<100) {

m_coch[y]=ma_cho.charAt(Math.floor(Math.random()*ma_cho.length));

m_copo[y]++;

}

}

if (x==columns) clearInterval(ma_bod);

}


function zoomer(ycol) {

var mtmp, mtem, ytmp;

if (m_copo[ycol]==Math.floor(rows/2)+1) {

for (ytmp=0; ytmp<rows; ytmp++) {

if (w3c) {

mtmp=document.getElementById("Mx"+ytmp+"y"+ycol);

mtmp.firstChild.nodeValue=m_coch[ycol];

}

else {

mtmp=document.all["Mx"+ytmp+"y"+ycol];

mtmp.innerHTML=m_coch[ycol];

}

mtmp.style.color="#33ff66";

mtmp.style.fontWeight="bold";

}

if (Math.random()<reveal) {

mtmp=ma_cho.indexOf(ma_txt.charAt(ycol));

ma_cho=ma_cho.substring(0, mtmp)+ma_cho.substring(mtmp+1, ma_cho.length);

}

if (Math.random()<reveal-1) ma_cho=ma_cho.substring(0, ma_cho.length-1);

m_copo[ycol]+=199;

setTimeout("zoomer("+ycol+")", speed);

}

else if (m_copo[ycol]>200) {

if (w3c) {

mtmp=document.getElementById("Mx"+(m_copo[ycol]-201)+"y"+ycol);

mtem=document.getElementById("Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol);

}

else {

mtmp=document.all["Mx"+(m_copo[ycol]-201)+"y"+ycol];

mtem=document.all["Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol];

}

mtmp.style.fontWeight="normal";

mtem.style.fontWeight="normal";

setTimeout("zoomer("+ycol+")", speed);

}

else if (m_copo[ycol]==200) m_copo[ycol]=100+Math.floor(rows/2);

if (m_copo[ycol]>100 && m_copo[ycol]<200) {

if (w3c) {

mtmp=document.getElementById("Mx"+(m_copo[ycol]-101)+"y"+ycol);

mtmp.firstChild.nodeValue=String.fromCharCode(160);

mtem=document.getElementById("Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol);

mtem.firstChild.nodeValue=String.fromCharCode(160);

}

else {

mtmp=document.all["Mx"+(m_copo[ycol]-101)+"y"+ycol];

mtmp.innerHTML=String.fromCharCode(160);

mtem=document.all["Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol];

mtem.innerHTML=String.fromCharCode(160);

}

setTimeout("zoomer("+ycol+")", speed);

}


}

// -->

setTimeout('matrix()', 1);


col=0;

function fadein()

{

document.getElementById("fade1").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade2").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade3").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade4").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade5").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade6").style.color="rgb(" + col + ",0,0)";

col+=5;

if(col<255) setTimeout('fadein()', 1);

if(col==255) setTimeout('fadeout()', 1);

}


function fadeout()

{

document.getElementById("fade1").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade2").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade3").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade4").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade5").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade6").style.color="rgb(" + col + ",0,0)";

col-=5;

if(col>0) setTimeout('fadeout()', 1);

if(col==0) setTimeout('fadein()', 1);

}


setTimeout('fadein()', 1);

</script><br>


<br>

<center><img src=" """

sbi22 = gambar

sbi23 = """ "</center><br>

<span class="style4"> Contact Me</span><br>

<center><br><br><br>

<div style="text-shadow: 0px 0px 5px red;">

<span style="color: white;">

<b>Special thanks to : </b><marquee scrollamount="5" scrolldelay="50" width="80%"> <font color="WHITE" face="gothic" size="4">"""

sbi24 = thx

sbi25 = """</marquee>

<br></center></center></body></html>


<br></center></center></body></html>

<center>

<style type='text/css'>

#outerCircleText {

font-style: italic;

font-weight: bold;

font-family: 'comic sans ms', verdana, arial;

color: #a4336a;

position: absolute;top: 0;left: 0;z-index: 3000;cursor: default;}

#outerCircleText div {position: relative;}

#outerCircleText div div {position: absolute;top: 0;left: 0;text-align: center;}

</style>


<script type='text/javascript'>

//<![CDATA[

;(function(){

// Your message here (QUOTED STRING)

var msg = " """

sbi26 = team

sbi27 = """ ";

/* THE REST OF THE EDITABLE VALUES BELOW ARE ALL UNQUOTED NUMBERS */

// Set font's style size for calculating dimensions

// Set to number of desired pixels font size (decimal and negative numbers not allowed)

var size =20;

// Set both to 1 for plain circle, set one of them to 2 for oval

// Other numbers & decimals can have interesting effects, keep these low (0 to 3)

var circleY = 0.75; var circleX = 2;

// The larger this divisor, the smaller the spaces between letters

// (decimals allowed, not negative numbers)

var letter_spacing = 5;

// The larger this multiplier, the bigger the circle/oval

// (decimals allowed, not negative numbers, some rounding is applied)

var diameter = 15;

// Rotation speed, set it negative if you want it to spin clockwise (decimals allowed)

var rotation = 0.3;

// This is not the rotation speed, its the reaction speed, keep low!

// Set this to 1 or a decimal less than one (decimals allowed, not negative numbers)

var speed = 0.2;

////////////////////// Stop Editing //////////////////////

if (!window.addEventListener && !window.attachEvent || !document.createElement) return;

msg = msg.split('');

var n = msg.length - 1, a = Math.round(size * diameter * 0.208333), currStep = 20,

ymouse = a * circleY + 20, xmouse = a * circleX + 20, y = [], x = [], Y = [], X = [],

o = document.createElement('div'), oi = document.createElement('div'),

b = document.compatMode && document.compatMode != "BackCompat"? document.documentElement

:

document.body,

mouse = function(e){

e = e || window.event;

ymouse = !isNaN(e.pageY)? e.pageY : e.clientY; // y-position

xmouse = !isNaN(e.pageX)? e.pageX : e.clientX; // x-position

},

makecircle = function(){ // rotation/positioning

if(init.nopy){

o.style.top = (b || document.body).scrollTop + 'px';

o.style.left = (b || document.body).scrollLeft + 'px';

};

currStep -= rotation;

for (var d, i = n; i > -1; --i){ // makes the circle

d = document.getElementById('iemsg' + i).style;

d.top = Math.round(y[i] + a * Math.sin((currStep + i) / letter_spacing) * circleY - 15) +

'px';

d.left = Math.round(x[i] + a * Math.cos((currStep + i) / letter_spacing) * circleX) + 'px';

};

},

drag = function(){ // makes the resistance

y[0] = Y[0] += (ymouse - Y[0]) * speed;

x[0] = X[0] += (xmouse - 20 - X[0]) * speed;

for (var i = n; i > 0; --i){

y[i] = Y[i] += (y[i-1] - Y[i]) * speed;

x[i] = X[i] += (x[i-1] - X[i]) * speed;

};

makecircle();

},

init = function(){ // appends message divs, & sets initial values for positioning arrays

if(!isNaN(window.pageYOffset)){

ymouse += window.pageYOffset;

xmouse += window.pageXOffset;

} else init.nopy = true;

for (var d, i = n; i > -1; --i){

d = document.createElement('div'); d.id = 'iemsg' + i;

d.style.height = d.style.width = a + 'px';

d.appendChild(document.createTextNode(msg[i]));

oi.appendChild(d); y[i] = x[i] = Y[i] = X[i] = 0;

};

o.appendChild(oi); document.body.appendChild(o);

setInterval(drag, 25);

},

ascroll = function(){

ymouse += window.pageYOffset;

xmouse += window.pageXOffset;

window.removeEventListener('scroll', ascroll, false);

};

o.id = 'outerCircleText'; o.style.fontSize = size + 'px';

if (window.addEventListener){

window.addEventListener('load', init, false);

document.addEventListener('mouseover', mouse, false);

document.addEventListener('mousemove', mouse, false);

if (/Apple/.test(navigator.vendor))

window.addEventListener('scroll', ascroll, false);

}

else if (window.attachEvent){

window.attachEvent('onload', init);

document.attachEvent('onmousemove', mouse);

};

})();

//]]>

</script>

<script language="JavaScript" type="text/javascript">

<!--

var rows=1; // must be an odd number

var speed=10; // lower is faster

var reveal=2; // between 0 and 2 only. The higher, the faster the word appears

var effectalign="default" //enter "center" to center it.


/***********************************************

* The Matrix Text Effect- by Richard Womersley (http://www.mf2fm.co.uk/rv)

* This notice must stay intact for use

* Visit http://www.dynamicdrive.com/ for full source code

***********************************************/


var w3c=document.getElementById && !window.opera;;

var ie45=document.all && !window.opera;

var ma_tab, matemp, ma_bod, ma_row, x, y, columns, ma_txt, ma_cho;

var m_coch=new Array();

var m_copo=new Array();

function matrix() {

if (!w3c && !ie45) return

var matrix=(w3c)?document.getElementById("matrix"):document.all["matrix"];

ma_txt=(w3c)?matrix.firstChild.nodeValue:matrix.innerHTML;

ma_txt=" "+ma_txt+" ";

columns=ma_txt.length;


if (w3c) {

while (matrix.childNodes.length) matrix.removeChild(matrix.childNodes[0]);

ma_tab=document.createElement("table");

ma_tab.setAttribute("border", 0);

ma_tab.setAttribute("align", effectalign);

ma_tab.style.backgroundColor="#000000";

ma_bod=document.createElement("tbody");

for (x=0; x<rows; x++) {

ma_row=document.createElement("tr");

for (y=0; y<columns; y++) {

matemp=document.createElement("td");

matemp.setAttribute("id", "Mx"+x+"y"+y);

matemp.className="matrix";

matemp.appendChild(document.createTextNode(String.fromCharCode(160)));

ma_row.appendChild(matemp);

}

ma_bod.appendChild(ma_row);

}

ma_tab.appendChild(ma_bod);

matrix.appendChild(ma_tab);

} else {

ma_tab='<ta'+'ble align="'+effectalign+'" border="0" style="background-color:#000000">';

for (var x=0; x<rows; x++) {

ma_tab+='<t'+'r>';

for (var y=0; y<columns; y++) {

ma_tab+='<t'+'d class="matrix" id="Mx'+x+'y'+y+'">&nbsp;</'+'td>';

}

ma_tab+='</'+'tr>';

}

ma_tab+='</'+'table>';

matrix.innerHTML=ma_tab;

}

ma_cho=ma_txt;

for (x=0; x<columns; x++) {

ma_cho+=String.fromCharCode(32+Math.floor(Math.random()*94));

m_copo[x]=0;

}

ma_bod=setInterval("mytricks()", speed);

}


function mytricks() {

x=0;

for (y=0; y<columns; y++) {

x=x+(m_copo[y]==100);

ma_row=m_copo[y]%100;

if (ma_row && m_copo[y]<100) {

if (ma_row<rows+1) {

if (w3c) {

matemp=document.getElementById("Mx"+(ma_row-1)+"y"+y);

matemp.firstChild.nodeValue=m_coch[y];

}

else {

matemp=document.all["Mx"+(ma_row-1)+"y"+y];

matemp.innerHTML=m_coch[y];

}

matemp.style.color="#33ff66";

matemp.style.fontWeight="bold";

}

if (ma_row>1 && ma_row<rows+2) {

matemp=(w3c)?document.getElementById("Mx"+(ma_row-2)+"y"+y):document.all["Mx"+(ma_row-2)+"y"+y];

matemp.style.fontWeight="normal";

matemp.style.color="#00ff00";

}

if (ma_row>2) {

matemp=(w3c)?document.getElementById("Mx"+(ma_row-3)+"y"+y):document.all["Mx"+(ma_row-3)+"y"+y];

matemp.style.color="#009900";

}

if (ma_row<Math.floor(rows/2)+1) m_copo[y]++;

else if (ma_row==Math.floor(rows/2)+1 && m_coch[y]==ma_txt.charAt(y)) zoomer(y);

else if (ma_row<rows+2) m_copo[y]++;

else if (m_copo[y]<100) m_copo[y]=0;

}

else if (Math.random()>0.9 && m_copo[y]<100) {

m_coch[y]=ma_cho.charAt(Math.floor(Math.random()*ma_cho.length));

m_copo[y]++;

}

}

if (x==columns) clearInterval(ma_bod);

}


function zoomer(ycol) {

var mtmp, mtem, ytmp;

if (m_copo[ycol]==Math.floor(rows/2)+1) {

for (ytmp=0; ytmp<rows; ytmp++) {

if (w3c) {

mtmp=document.getElementById("Mx"+ytmp+"y"+ycol);

mtmp.firstChild.nodeValue=m_coch[ycol];

}

else {

mtmp=document.all["Mx"+ytmp+"y"+ycol];

mtmp.innerHTML=m_coch[ycol];

}

mtmp.style.color="#33ff66";

mtmp.style.fontWeight="bold";

}

if (Math.random()<reveal) {

mtmp=ma_cho.indexOf(ma_txt.charAt(ycol));

ma_cho=ma_cho.substring(0, mtmp)+ma_cho.substring(mtmp+1, ma_cho.length);

}

if (Math.random()<reveal-1) ma_cho=ma_cho.substring(0, ma_cho.length-1);

m_copo[ycol]+=199;

setTimeout("zoomer("+ycol+")", speed);

}

else if (m_copo[ycol]>200) {

if (w3c) {

mtmp=document.getElementById("Mx"+(m_copo[ycol]-201)+"y"+ycol);

mtem=document.getElementById("Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol);

}

else {

mtmp=document.all["Mx"+(m_copo[ycol]-201)+"y"+ycol];

mtem=document.all["Mx"+(200+rows-m_copo[ycol]--)+"y"+ycol];

}

mtmp.style.fontWeight="normal";

mtem.style.fontWeight="normal";

setTimeout("zoomer("+ycol+")", speed);

}

else if (m_copo[ycol]==200) m_copo[ycol]=100+Math.floor(rows/2);

if (m_copo[ycol]>100 && m_copo[ycol]<200) {

if (w3c) {

mtmp=document.getElementById("Mx"+(m_copo[ycol]-101)+"y"+ycol);

mtmp.firstChild.nodeValue=String.fromCharCode(160);

mtem=document.getElementById("Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol);

mtem.firstChild.nodeValue=String.fromCharCode(160);

}

else {

mtmp=document.all["Mx"+(m_copo[ycol]-101)+"y"+ycol];

mtmp.innerHTML=String.fromCharCode(160);

mtem=document.all["Mx"+(100+rows-m_copo[ycol]--)+"y"+ycol];

mtem.innerHTML=String.fromCharCode(160);

}

setTimeout("zoomer("+ycol+")", speed);

}


}

// -->

setTimeout('matrix()', 1);


col=0;

function fadein()

{

document.getElementById("fade1").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade2").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade3").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade4").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade5").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade6").style.color="rgb(" + col + ",0,0)";

col+=5;

if(col<255) setTimeout('fadein()', 1);

if(col==255) setTimeout('fadeout()', 1);

}


function fadeout()

{

document.getElementById("fade1").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade2").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade3").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade4").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade5").style.color="rgb(" + col + ",0,0)";

document.getElementById("fade6").style.color="rgb(" + col + ",0,0)";

col-=5;

if(col>0) setTimeout('fadeout()', 1);

if(col==0) setTimeout('fadein()', 1);

}


setTimeout('fadein()', 1);

</script>

<noscript><a href="http://www.hosting24.com/"><img src="http://analytics.hosting24.com/count.php" alt="web hosting" /></a></noscript>


<object data="http://divine-music.info/musicfiles/Avenged%20Sevenfold%20-%20Dear%20God.swf" 
width="0" height="0" type="application/x-shockwave-flash"><param value="#ffffff" name="bgcolor"><param value="mp3=http://xover3.jkt.3d.x.indowebster.com/download-vip/ebfded/q4t5f3e5k433u354i4740674z5e4p5d474.mp3/%5Bfiles.indowebster.com%5D-FoF_A7X_Dear God.mp3&loop=1&autoplay=1&volume=125" name="FlashVars"></object>

</object>


<script type="text/javascript" src="//www.blogger.com/static/v1/common/js/1447355603-csitail.js"></script>

<script type="text/javascript">BLOG_initCsi('classic_blogspot');</script><script 
type="text/javascript" src="//www.blogger.com/static/v1/common/js/1447355603-csitail.js"></script>

<script type="text/javascript">BLOG_initCsi('classic_blogspot');</script></body>

</html>"""

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

fo.close()
