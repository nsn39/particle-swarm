from math import sin, cos, pi
import pygame
from pygame.locals import *

# constants
COLOR = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "grey": (16, 16, 16),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "gold": (255, 215, 0),
}
FPS = 30
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1200
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FONT_FILE = "resources/RobotoSlab-Regular.ttf"


def regular_polygon_points(vertex_count, radius, position) -> list:
    n, r = vertex_count, radius
    x, y = position
    points = [
        (x + r * cos(2 * pi * i / n),
         y + r * sin(2 * pi * i / n))
        for i in range(n)
    ]
    return points
