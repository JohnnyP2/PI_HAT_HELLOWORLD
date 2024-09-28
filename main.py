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

def pushed_down(event):
    sense.clear(0, 0, 0)
    print("Ending Program")
    exit()

sense.stick.direction_down = pushed_down

