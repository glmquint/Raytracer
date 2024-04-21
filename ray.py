from vec3 import *

class ray(object):
    def __init__(self, origin = vec3(), direction = vec3()):
        self.orig = origin
        self.dir = direction

    def at(self, t):
        return self.orig + t * self.dir
