import pygame

class Sprite:
    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None

    def move(self, dest, rect):
        new = rect.copy()
        new.x += dest[0]
        new.y += dest[1]
        return new

    def draw(self, surface, rect, texture):
        self.sc = surface
        self.sc.blit(texture, (rect.x, rect.y))

    def create_sprite(self, x, y, width, height, texture):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        rect = pygame.Rect(x, y, width, height)

        return rect

    def load_texture(self, filename):
       return pygame.image.load(filename)