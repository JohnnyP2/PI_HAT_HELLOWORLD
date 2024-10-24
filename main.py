import pi_art
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
# ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED allow button functions to work
sense = SenseHat()


'''
while True:
    sense.show_message("Hello world", text_colour=(0,255,0), back_colour=(0,0,255))
'''
picture = pi_art.artfiles() # get the pixels from the array in pi_art.py
sense.set_pixels(picture) # sets the sense hat to the pixels

#Uses the enviornment sensors on the sense hat to show the temperature, humidity, and pressure. then Displays the data on the LED matrix.
def enviSensor():
    sense.clear(0,0,0)
    temp = sense.get_temperature();
    humidity = sense.get_humidity();
    pressure = sense.get_pressure();
    print("Temperature: %s C" % temp)
    print("Humidity: %s %%" % humidity)
    print("Pressure: %s hPa" % pressure)

def compass():
    sense.clear(0,0,0)
    while True:
        north = sense.get_compass()
        # get current device orientation, the yaw of the device
        # compare north to the yaw of the device
        # change the rotation of the device to make the image point north.



def pushed_down(event):
    sense.clear(0, 0, 0)
    print("Ending Program")
    exit()
while True:
    sense.stick.direction_down = pushed_down

