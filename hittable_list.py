from hittable import *

class hittable_list(hittable):

    def __init__(self):
        self.objects = []
    
    def add(self, obj):
        self.objects.append(obj)

    def clear(self):
        self.objects = []

    def hit(self, r, t_min, t_max, rec):
        temp_rec = [hit_record()]
        hit_anything = False
        closest_so_far = t_max

        for obj in self.objects:
            if obj.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec[0].t
                rec[0] = temp_rec[0]

        return hit_anything
