#!bin/bash
#rem (c) DL2SBA 2018
now=`date +%Y%m%d_%H%M%S`
java -Dfstart=1000000 -Dfstop=30000000 -Dfsteps=500 -DdriverId=20 -DdriverPort=ttyUSB0 -Daverage=1 -Dcalfile=vnaJ.3.2/calibration/REFL_miniVNA-Tiny.cal -Dscanmode=REFL -Dexports=xls -DexportDirectory=vnaJ.3.2/export/ -DexportFilename=VNA_A0_$now -DkeepGeneratorOn -jar /home/pi/vnaJ.3.2/vnaJ-hl.3.2.10.jar
python ~/vnaJ.3.2/importFromExcel.py /home/pi/vnaJ.3.2/export/VNA_A0_$now.xls
rm /home/pi/vnaJ.3.2/export/VNA_A0_$now.xls
bash /home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/vnaJ.3.2/export/VNA_A0_$now.txt /VNA_A0_$now.txt
