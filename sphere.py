from hittable import *
from vec3 import *
from math import sqrt
from eprint import *

class sphere(hittable):
    def __init__(self, cen, r, m):
        self.center = cen
        self.radius = r
        self.mat_ptr = m

    def hit(self, r, t_min, t_max, rec):
        oc = r[0].orig - self.center
        a = r[0].dir.length_squared()
        half_b = vec3.dot(oc, r[0].dir)
        c = oc.length_squared() - self.radius * self.radius

        discriminant = half_b * half_b - a*c
        if discriminant < 0:
            return False
        sqrtd = sqrt(discriminant)

        # find the nearest root that lies in the acceptable range
        assert a != 0, f'{r[0]}'
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b - sqrtd) / a
            if root < t_min or t_max < root:
                return False

        rec[0].t = root
        rec[0].p = r[0].at(rec[0].t)
        outward_normal = (rec[0].p - self.center) / self.radius
        rec[0].set_face_normal(r[0], outward_normal)
        rec[0].mat_ptr = self.mat_ptr

        return True
