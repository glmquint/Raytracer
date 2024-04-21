from eprint import *
from math import sqrt, inf, pi, cos
from random import random
from random import uniform
from color import *
from hittable_list import *
from ray import *
from material import *
from sphere import *
from camera import *

def ray_color(r, world, depth):
    # if we exceeded the ray bounce limit, no more light is gathered
    if depth <= 0:
        return color(0, 0, 0)

    rec = [hit_record()]
    if world.hit(r, 0.001, inf, rec):
        #target = rec[0].p + rec[0].normal + vec3.random_unit_vector()
        #target = rec[0].p + vec3.random_in_hemisphere(rec[0].normal)
        #return 0.5 * ray_color(ray(rec[0].p, target - rec[0].p), world, depth - 1)
        scattered = [ray()]
        attenuation = [color()]
        if rec[0].mat_ptr.scatter(r, rec, attenuation, scattered):
            return attenuation[0] * ray_color(scattered, world, depth - 1)
        return color(0, 0, 0)
    unit_direction = vec3.unit_vector(r[0].dir)
    t = 0.5 * (unit_direction.y + 1)
    return (1 - t) * color(1, 1, 1) + t * color(0.5, 0.7, 1)

def random_scene():
    world = hittable_list()
    material_ground = lambertian(color(0.5, 0.5, 0.5))
    world.add(sphere(point3(0, -1000, 0), 1000, material_ground))

    for a in range(-11, 11, 1):
        for b in range(-11, 11, 1):
            choose_mat = random()
            center = point3(a + 0.9 * random(), 0.2, b + 0.9 * random())

            if (center - point3(4, 0.2, 0)).length() > 0.9:
                sphere_material = material()

                if choose_mat < 0.8:
                    albedo = color.random() * color.random()
                    sphere_material = lambertian(albedo)
                    world.add(sphere(center, 0.2, sphere_material))
                elif choose_mat < 0.95:
                    albedo = color.random_uniform(0.5, 1)
                    fuzz = uniform(0, 0.5)
                    sphere_material = metal(albedo, fuzz)
                    world.add(sphere(center, 0.2, sphere_material))
                else:
                    sphere_material = dielectric(1.5)
                    world.add(sphere(center, 0.2, sphere_material))

    material1 = dielectric(1.5)
    world.add(sphere(point3(0, 1, 0), 1.0, material1))

    material2 = lambertian(color(0.4, 0.2, 0.1))
    world.add(sphere(point3(-4, 1, 0), 1.0, material2))

    material3 = metal(color(0.7, 0.6, 0.5), 0.0)
    world.add(sphere(point3(4, 1, 0), 1.0, material3))

    return world

def main():
    # image
    aspect_ratio = 3/2
    img_width = 400
    img_height = int(img_width / aspect_ratio)
    samples_per_pixel = 100
    max_depth = 10

    # world
    world = random_scene()

    #R = cos(pi/4)
    #material_left = lambertian(color(0, 0, 1))
    #material_right = lambertian(color(1, 0, 0))

    #world.add(sphere(point3(-R, 0, -1), R, material_left))
    #world.add(sphere(point3( R, 0, -1), R, material_right))

    # camera
    lookfrom = point3(13, 2, 3)
    lookat = point3(0, 0, 0)
    vup = vec3(0, 1, 0)
    dist_to_focus = 10
    aperture = 0.1
    cam = camera(lookfrom, lookat, vup, 20, aspect_ratio, aperture, dist_to_focus)

    # render
    print(f"P3\n{img_width} {img_height}\n255")
    for j in range(img_height-1, -1, -1):
        for i in range(img_width):
            eprint(f"\r{(img_height - j)/img_height:.2%} {i/img_width:.2%}", end='')
            pixel_color = color(0, 0, 0)
            for s in range(samples_per_pixel):
                u = (i + random()) / (img_width - 1)
                v = (j + random()) / (img_height - 1)
                r = [cam.get_ray(u, v)]
                pixel_color = pixel_color + ray_color(r, world, max_depth)

            write_color(pixel_color, samples_per_pixel)
    eprint("\nDone!")

if __name__ == '__main__':
    main()
