import pygame

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __iadd__(self, other):
        self.x = other.x
        self.y = other.y
        return self

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)