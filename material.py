from vec3 import *
from ray import *
from color import *
from random import random as random_double

class material(object):
    def scatter(self, r_in, rec, attenuation, scattered):
        pass

class lambertian(material):
    def __init__(self, a):
        self.albedo = a

    def scatter(self, r_in, rec, attenuation, scattered):
        scatter_direction = rec[0].normal + vec3.random_unit_vector()
        # catch degenerate scatter direction
        if scatter_direction.near_zero():
            scatter_direction = rec[0].normal

        scattered[0] = ray(rec[0].p, scatter_direction)
        attenuation[0] = self.albedo
        return True

class metal(material):
    def __init__(self, a, f):
        self.albedo = a
        self.fuzz = f if f < 1 else 1

    def scatter(self, r_in, rec, attenuation, scattered):
        reflected = vec3.reflect(vec3.unit_vector(r_in[0].dir), rec[0].normal)

        scattered[0] = ray(rec[0].p, reflected + self.fuzz * vec3.random_in_unit_sphere())
        attenuation[0] = self.albedo
        return (vec3.dot(scattered[0].dir, rec[0].normal) > 0)

class dielectric(material):
    def __init__(self, index_of_refraction):
        self.ir = index_of_refraction

    @staticmethod
    def reflectance(cosine, ref_idx):
        r0 = (1-ref_idx) / (1+ref_idx)
        r0 = r0 * r0
        return r0 + (1-r0) * pow((1 - cosine), 5)

    def scatter(self, r_in, rec, attenuation, scattered):
        attenuation[0] = color(1, 1, 1)
        refraction_ratio = (1/self.ir) if rec[0].front_face else self.ir

        unit_direction = vec3.unit_vector(r_in[0].dir)
        cos_theta = min(vec3.dot(-unit_direction, rec[0].normal), 1.0)
        sin_theta = sqrt(1 - cos_theta * cos_theta)

        cannot_refract = refraction_ratio * sin_theta > 1
        direction = vec3()

        if cannot_refract or self.reflectance(cos_theta, refraction_ratio) > random_double():
            direction = vec3.reflect(unit_direction, rec[0].normal)
        else:
            direction = vec3.refract(unit_direction, rec[0].normal, refraction_ratio)

        scattered[0] = ray(rec[0].p, direction)
        return True

