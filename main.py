import pi_art
import time
import threading as th
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
# ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED allow button functions to work
sense = SenseHat()
'''
TODO
    - Add a way to change the art also add more art to artfiles
    - Show temp on led matrix
    - break out of while loops when button is pressed for the applications
    - verify everything is functional
'''
#Uses the enviornment sensors on the sense hat to show the temperature, humidity, and pressure. then Displays the data on the LED matrix.
def enviSensor():
    sense.clear(0,0,0)
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    print("Temperature: %s C" % temp)
    print("Humidity: %s %%" % humidity)
    print("Pressure: %s hPa" % pressure)

def compass():
    sense.clear(0,0,0)
    sense.show_letter("i") # placeholder for a compass arrow
    while True:
        heading = sense.get_compass()
        # get current device orientation, the yaw of the device
        # compare north to the yaw of the device
        # change the rotation of the device to make the image point north.
        print("Current Direction: " + heading)
        time.sleep(0.5)
        if(heading < 45 or heading > 315):
            sense.set_rotation(0)
        elif(heading < 135):
            sense.set_rotation(90)
        elif(heading < 225):
            sense.set_rotation(180)
        elif(heading < 315):
            sense.set_rotation(270)
def showArt():            
    picture = pi_art.artfiles() # get the pixels from the array in pi_art.py
    sense.set_pixels(picture) # sets the sense hat to the pixels

def end():
    sense.clear(0, 0, 0)
    print("Ending Program")
    exit()


#while loop that shows a message as the entry point for the program
while True:
    sense.show_message("press up for art, left for compass, right for temp, and down to end program!", text_colour=(0,255,0), back_colour=(0,0,255))
    event = sense.stick.get_events()
    if event.direction == 'middle':
        sense.show_message("Hello world", text_colour=(0,255,0), back_colour=(0,0,255))
    elif event.direction == 'up':
        showArt()
    elif event.direction == 'down':
        end()
    elif event.direction == 'left':
        compass()
    elif event.direction == 'right':
        enviSensor()


