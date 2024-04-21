from ray import *
from vec3 import *
from color import *
from math import radians as degrees_to_radians
from math import tan

class camera(object):
    def __init__(self, lookfrom, lookat, vup, vfov, aspect_ratio, aperture, focus_dist):
        theta = degrees_to_radians(vfov)
        h = tan(theta/2)
        viewport_height = 2 * h
        viewport_width = aspect_ratio * viewport_height

        self.w = vec3.unit_vector(lookfrom - lookat)
        self.u = vec3.unit_vector(vec3.cross(vup, self.w))
        self.v = vec3.cross(self.w, self.u)

        self.origin = lookfrom
        self.horizontal = focus_dist * viewport_width * self.u
        self.vertical = focus_dist * viewport_height * self.v
        self.lower_left_corner = self.origin - self.horizontal/2 - self.vertical/2 - focus_dist * self.w

        self.lens_radius = aperture / 2

    def get_ray(self, s, t):
        rd = self.lens_radius * vec3.random_in_unit_disk()
        offset = self.u * rd.x + self.v * rd.y
        return ray(self.origin + offset, self.lower_left_corner + s * self.horizontal + t * self.vertical - self.origin - offset)

