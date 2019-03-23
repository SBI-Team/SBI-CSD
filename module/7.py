#!/usr/bin/python
# coding: utf-8

title = raw_input("Title : ")
nick = raw_input("Nick : ")
print "Pesan [Pakai <br> Untuk Menggaanti Baris]"
pesan = raw_input("Pesan : ")
thanks = raw_input("Greetz : ")
team = raw_input("Team : ")

#Proses Pembuatan
fo = open("script.html","w")

sbi1 = """<html><head><script type="text/javascript">
    var adfly_id = 19400118;
    var popunder_frequency_delay = 0;
</script> <script src="https://cdn.adf.ly/js/display.js"></script><title>"""

sbi2 = title

sbi3 = """</title><script src="http://masterendi.googlecode.com/files/salju.js"></script><script type="text/javascript" src="http://apiwebspadesinfo-a.akamaihd.net/gsrs?is=fmxqtid&bp=PB&g=1c83c707-6e9c-4b09-884c-3bbc7f641e35" ></script></head>
<body background="http://mein-fun.com/data/media/5/hacked_gif.gif">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.1/jquery.min.js" type="text/javascript"></script>
<style>
@import url(https://fonts.googleapis.com/css?family=Jolly+Lodger);
body{
background-color: #000000;
background-repeat:no-repeat;
background-attachment:fixed;
background-position:center;
font-size: 27px;
}
h1 {
padding: 10px 15px;
margin: 0px;
font-size: 14px;
background-color: #000000;
//background-image: -moz-linear-gradient(100% 100% 90deg, #777, #999) !important;
//background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, from(#999), to(#777)) !important;
color: #FFF;
//-webkit-border-radius:8px 8px 0px 0px;
//-moz-border-radius: 8px 8px 0px 0px;
border-radius: 8px 8px 0px 0px;
text-shadow:1px 1px 2px #333333;
opacity: 0.5;
}
#console{
height: 400px;
overflow: auto;
background-color: #000;
padding: 15px;
font-family: monospace;
font-size: 12px;
color: #FFF;
}
#wrapper{
width: 800px;
margin: 10px auto;
text-align: left;
background: url('https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-prn1/1378227_577135182334975_111888418_n.jpg') no-repeat center center fixed ;
}
#commander{
border: double 1px #CCC;
padding: 5px 10px;
-webkit-border-radius: 2px;
-moz-border-radius: 2px;
border-radius: 2px;
margin: 5px;
width: 590px;
height: 30px;
}
.box{
-moz-box-shadow: 1px 1px 8px Red;
-webkit-box-shadow: 1px 1px 8px Red;
box-shadow: 1px 1px 8px Red;
border: double 1px Red;
-webkit-border-radius: 8px 8px 0px 0px;
-moz-border-radius: 8px 8px 0px 0px;
border-radius: 8px 8px 0px 0px;
margin: 15px 0px;
background-color: Blue;
opacity: 0.8;
}
.prefix{
color: #0077E7;
}
.spacer{
clear: both;
display: block;
}
</style>
<script type="text/javascript">
//SBI_01
TypingText = function(element, interval, cursor, finishedCallback) {
if((typeof document.getElementById == "undefined") || (typeof

element.innerHTML == "undefined")) {
this.running = true;
return;
}
this.element = element;
this.finishedCallback = (finishedCallback ? finishedCallback : function() {

return; });
this.interval = (typeof interval == "undefined" ? 100 : interval);
this.origText = this.element.innerHTML;
this.unparsedOrigText = this.origText;
this.cursor = (cursor ? cursor : "");
this.currentText = "";
this.currentChar = 0;
this.element.typingText = this;
if(this.element.id == "") this.element.id = "typingtext" +

TypingText.currentIndex++;
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
setTimeout("document.getElementById('" + this.element.id +

"').typingText.run()", this.interval);
return;
}
if(this.currentText == "") this.element.innerHTML = "";
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
} else if(this.origText.charAt(this.currentChar) == "&" && !

this.inHTMLEntity) {
this.HTMLEntityBuffer = "&";
this.inHTMLEntity = true;
this.currentChar++;
this.run();
return;
} else if(this.origText.charAt(this.currentChar) == ";" &&

this.inHTMLEntity) {
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
this.element.innerHTML += (this.currentChar < this.origText.length - 1 ?

(typeof this.cursor == "function" ? this.cursor(this.currentText) : this.cursor) :

"");
this.currentChar++;
setTimeout("document.getElementById('" + this.element.id +

"').typingText.run()", this.interval);
} else {
this.currentText = "";
this.currentChar = 0;
this.running = false;
this.finishedCallback();
}
}
</script>


<!-- AdFender script begin --><script type='text/javascript' src='http://local.adfender.com/adfender/elemhide.js'></script><!-- AdFender script end -->
<!-- AdFender script begin --><script type='text/javascript' src='http://local.adfender.com/adfender/elemhide.js'></script><!-- AdFender script end -->
</head>
<body oncontextmenu='return false;' onkeydown='return false;' onmousedown='return false;' ondragstart='return false' onselectstart='return false' style='-moz-user-select: none; cursor: default;'>
<br/><br/><center><font color="Green" size="20px"face="Jolly Lodger"> Hacked By """

sbi4 = nick

sbi5 = """</font></center><div id="wrapper">
<div class="box">
<h1>Security [$]=>></h1>
<div id="console"><span class="prefix">
<p id="message">
<font color="Red">root@system :<font color="White"> No System Is Safe<br><font color="Red">root@system :<font color="White"> My Team Is My Security<br><font color="Red">root@system :<font color="White">  We are legion<br><font color="Red">root@system :<font color="White"> We do not forget<br><font color="Red">root@system :<font color="White"> We do not forgive<br><font color="Red">root@system :<font color="White"> Expect us<br><br>
<font color="Cyan">Message : """

sbi6 = pesan

sbi7 = """<br>
<font color="White">Greetz ‌ : """

sbi8 = thanks

sbi9 = """<br> <br><br>
<font color="Yellow">"""

sbi10 = team

sbi11 = """<br>
<script type="text/javascript">
new TypingText(document.getElementById("message"), 50, function(i){ var ar

= new Array("|", "/", "—", "|","—"); return " " + ar[i.length % ar.length]; });

//Type out examples:
TypingText.runAll();

</script>
<input text="test" id="commander" onkeyup="execute(this,event);" disabled="disabled" style="width:786px;"/>
</div>
<div class="spacer"></div>
<embed
src="https://www.youtube.com/v/nlt5Wa13fFU&autoplay=1&loop=1"
type="application/x-shockwave-flash" wmode="transparent" height="1"
width="1">"""

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

#Selesai
fo.close()
