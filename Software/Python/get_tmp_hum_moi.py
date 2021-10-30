#!/usr/bin/env python

import grovepi
import math
import time
import sqlite3

con = sqlite3.connect('/home/pi/workspace/tmp_hum_moi_log.db')

# cur = con.cursor()
# cur.execute("INSERT INTO lab_env_log (time, tmp, hum, moi) VALUES (datetime('now', 'localtime'), %f, %f, %f);" % (temp, humidity, grovepi.analogRead(sensor)))

# con.commit()
# con.close()


# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 4  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

#def get_tem_hum(sensor,white):
    
while True:
    import grovepi 
    try:
        # This example uses the blue colored sensor. 
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(sensor, white)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
            break
        print([temp,humidity])

    except IOError:
        print ("Error")


# NOTE:
#       The wiki suggests the following sensor values:
#               Min  Typ  Max  Condition
#               0    0    0    sensor in open air
#               0    20   300  sensor in dry soil
#               300  580  700  sensor in humid soil
#               700  940  950  sensor in water
        
#       Sensor values observer: 
#               Val  Condition
#               0    sensor in open air
#               18   sensor in dry soil
#               425  sensor in humid soil
#               690  sensor in water

# Connect the Grove Moisture Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = 2

try:
    print(grovepi.analogRead(sensor))
    time.sleep(.5)

except KeyboardInterrupt:
    pass
except IOError:
    print ("Error")


cur = con.cursor()
cur.execute("INSERT INTO lab_env_log (time, tmp, hum, moi) VALUES (datetime('now', 'localtime'), %f, %f, %f);" % (temp, humidity, grovepi.analogRead(sensor)))

con.commit()
con.close()
