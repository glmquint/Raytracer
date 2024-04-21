from vec3 import *
from numpy import clip as clamp
from math import sqrt

class point3(vec3):
    pass

class color(vec3):
    pass

def write_color(pixel_color, samples_per_pixel):
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z

    scale = 1 / samples_per_pixel
    r = sqrt(r * scale)
    g = sqrt(g * scale)
    b = sqrt(b * scale)

    print(f"{int(255.999 * clamp(r, 0, 0.999))} {int(255.999 * clamp(g, 0, 0.999))} {int(255.999 * clamp(b, 0, 0.999))}")
