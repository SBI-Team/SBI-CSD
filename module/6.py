#!/usr/bin/python
# coding: utf-8

title = raw_input("Title : ")
nick = raw_input("Nick : ")
team = raw_input("Team : ")

fo = open("script.html","w")

sbi1 = """<html><head><title>"""

sbi2 = title

sbi3 = """</title></style><script type="text/javascript">
    var adfly_id = 19400118;
    var popunder_frequency_delay = 0;
</script>
<script src="https://cdn.adf.ly/js/display.js"></script><style>
@import url(https://fonts.googleapis.com/css?family=Sedgwick+Ave+Display);
@import url(https://fonts.googleapis.com/css?family=Jolly+Lodger);
@import url(https://fonts.googleapis.com/css?family=Iceberg);
</style></head><body bgcolor="Black"><br><br><br><br><br><br><center><font color="Black" size="100" face="Sedgwick Ave Display" style="text-shadow: Red 0px 2px 6px;">::: Hacked By """

sbi4 = nick

sbi5 = """ :::</font><br><br><br><font color="Yellow" size="3" face="Iceberg" style="text-shadow: Yellow 0px 1px 3px;">.:: My Team Is My Security ::.</font><br><font color="White" size="3" face="Iceberg" style="text-shadow: White 0px 1px 3px;">.:: No System Is Safe ::.</font><br><br><font color="Red" size="5" face="Jolly Lodger" style="-webkit-text-stroke: 1px White;">"""

sbi6 = team

sbi7 = """</font></center></body></html>"""

fo.write(sbi1)
fo.write(sbi2)
fo.write(sbi3)
fo.write(sbi4)
fo.write(sbi5)
fo.write(sbi6)
fo.write(sbi7)

fo.close()
