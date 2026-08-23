import pygame

class Transform():
    def __init__(self):
        pass

    def scale(self, dest, src):
        return pygame.transform.scale(src, dest)

    def rotate(self, angle, src):
        return pygame.transform.rotate(src, angle)

    def flip(self, surface, flip_x, flip_y):
        return pygame.transform.flip(surface, flip_x, flip_y)