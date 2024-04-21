from math import sqrt
from random import random as random_double
from random import uniform

class vec3(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def dot(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross(v1, v2):
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.z * v2.x - v1.x * v2.z
        z = v1.x * v2.y - v1.y * v2.x
        return vec3(x, y, z)

    @staticmethod
    def unit_vector(v):
        return v / v.length()

    def length(self):
        return sqrt(vec3.dot(self, self))

    def length_squared(self):
        return vec3.dot(self, self)

    def __add__(self, v):
        return vec3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)

    def __sub__(self, v):
        return self + (-v)

    def __mul__(self, v):
        if isinstance(v, vec3):
            return vec3(self.x * v.x, self.y * v.y, self.z * v.z)
        else:
            #assert type(self.x) == float or int,  f'componenti {self.x} solo float invece che {type(self.x)}'
            #assert type(self.y) == float or int, f'componenti {self.y} solo float invece che {type(self.y)}'
            #assert type(self.z) == float or int, f'componenti {self.z} solo float invece che {type(self.z)}'
            #assert type(v) == float, f'{v}'
            return vec3(self.x * v, self.y * v, self.z * v)

    def __rmul__(self, v):
        return self.__mul__(v)

    def __truediv__(self, v):
        if isinstance(v, vec3):
            return vec3(self.x / v.x, self.y / v.y, self.z / v.z)
        else:
            return vec3(self.x / v, self.y / v, self.z / v)

    def __str__(self):
        return '[ %.4f, %.4f, %.4f ]' % (self.x, self.y, self.z)

    @staticmethod
    def random():
        return vec3(random_double(), random_double(), random_double())

    @staticmethod
    def random_uniform(min_val, max_val):
        return vec3(uniform(min_val, max_val), uniform(min_val, max_val), uniform(min_val, max_val))

    @staticmethod
    def random_in_unit_sphere():
        while True:
            p = vec3.random_uniform(-1, 1)
            if p.length_squared() >= 1:
                continue
            return p

    @staticmethod
    def random_unit_vector():
        return vec3.unit_vector(vec3.random_in_unit_sphere())

    @staticmethod
    def random_in_hemisphere(normal):
        in_unit_sphere = vec3.random_in_unit_sphere()
        if vec3.dot(in_unit_sphere, normal) > 0:
            return in_unit_sphere
        else:
            return -in_unit_sphere

    def near_zero(self):
        s = 1e-8
        return (abs(self.x) < s) and (abs(self.y) < s) and (abs(self.z) < s)

    @staticmethod
    def reflect(v, n):
        return v - 2 * vec3.dot(v, n) * n

    @staticmethod
    def refract(uv, n, etai_over_etat):
        cos_theta = min(vec3.dot(-uv, n), 1.0)
        r_out_perp = etai_over_etat * (uv + cos_theta * n)
        r_out_parallel = -sqrt(abs(1 - r_out_perp.length_squared())) * n
        return r_out_perp + r_out_parallel

    @staticmethod
    def random_in_unit_disk():
        while True:
            p = vec3(uniform(-1, 1), uniform(-1, 1), 0)
            if p.length_squared() >= 1:
                continue
            return p

