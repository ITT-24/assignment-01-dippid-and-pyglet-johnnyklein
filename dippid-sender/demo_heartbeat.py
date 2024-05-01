from time import sleep

from DIPPID import SensorUDP

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)


print('capabilities: ', sensor.get_capabilities())
def handle_button_press(data):
    if int(data) == 0:
        print('button released')
    else:
        print('button pressed')


sensor.register_callback('button_1', handle_button_press)

while True:
# check if the sensor has the 'accelerometer' capability
    if sensor.has_capability('accelerometer'):
        # print whole accelerometer object (dictionary)
        print('accelerometer data: ', sensor.get_value('accelerometer'))

         # print only one accelerometer axis
        print('accelerometer X: ', sensor.get_value('accelerometer')['x'])

        sleep(0.1)
