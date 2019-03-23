#!/bin/sh
clear
cd ../Hasil
read -p "Nama Script [ex:SBI.html] : " nama
read -p "Nick : " nick
sleep 1
echo "Please Wait"
sleep 1
printf """<html><head><title>Error 404 Not found</title><script type="text/javascript">     var adfly_id = 19400118;     var popunder_frequency_delay = 0; </script> <script src="https://cdn.adf.ly/js/display.js"></script><meta http-equiv="refresh" content="40"></head><body><right><h1 color="Black"><b>Error</b></h1><hr color="Black"><h3 color="Black">404 Not found</h3><hr color="Black"><br><font color="Black"><b>$nick</b> Was Here</font></body></html>""" >> $nama
echo "Done Create"
echo -e "Cek di\033[36;1m `pwd`"
