from vec3 import *
from color import *

class hit_record:
    def __init__(self, p=point3(), normal=vec3(), t=0):
        self.p = p
        self.normal = normal
        self.t = t
        self.mat_ptr = 0

    def set_face_normal(self, r, outward_normal):
        self.front_face = vec3.dot(r.dir, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

class hittable(object):
    def hit(self, r, r_min, r_max, rec):
        return 0
