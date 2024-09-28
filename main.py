import pi_art
from sense_hat import SenseHat
sense = SenseHat()


'''
while True:
    sense.show_message("Hello world", text_colour=(0,255,0), back_colour=(0,0,255))
'''
sense.set_pixels(pi_art.art_files)