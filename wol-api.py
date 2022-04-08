from sensorhub.hub import SensorHub        # Library to read from DockerPi/52Pi EP-0106
from datetime import datetime              # To get GMT local timestamp
import time                                # To wait between readings
import csv                                 # Append data to csv

# Assume that anti-frost heating is not on
frost_on = False

# Clear sensor readings dictionary
readings = {}

def get_readings():

    # SensorHub instance
    hub = SensorHub()

    # Datetime stamp
    dt = datetime.now().strftime('%d-%b-%Y %H:%M:%S')

    # Dictionary of sensor readings
    global readings
    readings = {
        'Reading Datetime (GMT)' : dt,
        'Off Board Temperature (oC)' : hub.get_off_board_temperature(),
        'Humidity (%)' : hub.get_humidity(),
        'Motion Detected (T/F)' : hub.is_motion_detected(),
        'Brightness (lm)' : hub.get_brightness(),
        'Board Temperature (oC)' : hub.get_temperature(),
        'Barometer Pressure (mb)' : hub.get_barometer_pressure(),
        'Barometer Temperature (oC)' : hub.get_barometer_temperature()
        }


def log_readings():
    
    # Append data to csv (add headers if required)
    headers = readings.keys()
    with open('readings.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=readings.keys())
        if f.tell() == 0:
            writer.writeheader()

        writer.writerow(readings)


def frost_check(min_temp, max_temp):

    # Turn heating on if temp <2 oC or
    # turn heating off if temp >2
    if data['Off Board Temperature (oC)'] < min_temp and frost_on == False:
        # heating on
        print('test')
        
    elif data['Off Board Temperature (oC)'] >= max_temp and frost_on == True:
        # heating off
        print('test')


def call_monkey(monkey,announcement = ' '):

    PAT = '970f7c8f32b261b84dedd33ba2f77ee1'
    ST = '43e69e6ade59dff6bc96b9531ab12a3f'

    announcement.replace(' ','%20')
    url = 'https://api.voicemonkey.io/trigger?access_token=' + PAT + '&secret_token=' + ST + '&monkey=' + monkey + '&announcement=' + announcement

    requests.get(url)


# Loop program (reading every five minutes)
while True:
    for i in range(60*5):
        time.sleep(1)

    # Execute tasks    
    get_readings()             # Get sensor data
    log_readings()             # Save data to CSV
    # frost_check(3, 5)              # Turn on heating if frosty (lowest temp, restore to temp)