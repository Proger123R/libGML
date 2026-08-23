import pygame

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

    def apply(self, x, y):
        return x - self.x, y - self.y

    def follow(self, rect, surface):
        self.x = rect.x - surface.get_width() / 2
        self.y = rect.y - surface.get_height() / 2

    def player(self, rect):
        new = rect.copy()
        new.x += rect.x - self.x
        new.y += rect.y - self.y
        return new