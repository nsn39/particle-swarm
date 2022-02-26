from math import sin, cos, pi
import pygame
from pygame.locals import *

# constants
COLOR = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
}
FPS = 30
SCREEN_SIZE = (800, 800)


def regular_polygon_points(vertex_count, radius, position) -> list:
    n, r = vertex_count, radius
    x, y = position
    points = [
        (x + r * cos(2 * pi * i / n),
         y + r * sin(2 * pi * i / n))
        for i in range(n)
    ]
    return points