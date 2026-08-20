import pygame

class Keyboard:
    def __init__(self):
        self.keyses = {
            "W": pygame.K_w,
            "A": pygame.K_a,
            "S": pygame.K_s,
            "D": pygame.K_d,
            "Q": pygame.K_q,
            "E": pygame.K_e,
            "R": pygame.K_r,
            "T": pygame.K_t,
            "U": pygame.K_u,
            "V": pygame.K_v,
            "UP": pygame.K_UP,
            "DOWN": pygame.K_DOWN,
            "LEFT": pygame.K_LEFT,
            "RIGHT": pygame.K_RIGHT
        }
        self.keys = pygame.key.get_pressed()
    
    def is_pressed(self, key) -> bool:
        self.keys = pygame.key.get_pressed()
        if not self.keys[self.keyses.get(key)]:
            return False
        return self.keys[self.keyses[key]]

    def update(self):
        pass

    def get_pressed(self):
        return self.keys