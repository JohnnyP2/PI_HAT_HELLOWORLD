from sense_hat import SenseHat
sense = SenseHat()

def artfiles():
    b = (0, 0, 0) # black
    r = (255, 0, 0) # red
    g = (0, 255, 0) # green
    bl = (0, 0, 255) # blue
    w = (255,255,255) # white

    jack_frost = {
        bl, w, w, w, w, w, w, bl,
        bl, w, b, w, w, b, w, bl,
        bl, w, b, w, w, b, w, bl,
        w, w, w, w, w, w, w, w,
        w, b, w, b, b, w, b, w,
        w, b, b, b, b, b, b, w,
        w, w, b, b, b, b, w, w,
        w, w, w, w, w, w, w, w
    }
    return jack_frost