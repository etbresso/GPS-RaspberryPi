import gps
import os
import time
import datetime
from Adafruit_7Segment import SevenSegment
     
os.system("sudo killall gpsd")
os.system("sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock")	 

segment = SevenSegment(address=0x70)
	 	 
# Ecouter sur le port 2947 (gpsd) de localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    	 
while True:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'speed'):
				print report.speed
				vitesse = report.speed * 3.6
				segment.writeDigit(1, int(vitesse / 10)) 
				if int(vitesse % 10) == 0 : segment.writeDigitRaw(3, 63+128)
				if int(vitesse % 10) == 1 : segment.writeDigitRaw(3, 6+128)
				if int(vitesse % 10) == 2 : segment.writeDigitRaw(3, 91+128)
				if int(vitesse % 10) == 3 : segment.writeDigitRaw(3, 79+128)
				if int(vitesse % 10) == 4 : segment.writeDigitRaw(3, 102+128)
				if int(vitesse % 10) == 5 : segment.writeDigitRaw(3, 109+128)
				if int(vitesse % 10) == 6 : segment.writeDigitRaw(3, 125+128)
				if int(vitesse % 10) == 7 : segment.writeDigitRaw(3, 7+128)
				if int(vitesse % 10) == 8 : segment.writeDigitRaw(3, 127+128)
				if int(vitesse % 10) == 9 : segment.writeDigitRaw(3, 111+128)
				segment.writeDigit(4, int((vitesse *10)%10)) # Ones
    except KeyError:
       pass
    except KeyboardInterrupt:
       quit()
    except StopIteration:
       session = None
       print "GPSD est arrete (has terminated)"