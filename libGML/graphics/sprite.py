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

    def draw(self, surface, rect, texture, camera=None):
        self.sc = surface
        if camera:
            x = rect.x - camera.x
            y = rect.y - camera.y
        else:
            x = rect.x
            y = rect.y
        self.sc.blit(texture, (x, y))

    def create_sprite(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        rect = pygame.Rect(x, y, width, height)

        return rect

    def load_texture(self, filename):
       return pygame.image.load(filename)

    def get_frame(self, frames, current_index, dt, delay=0.1, step=1):
        if not hasattr(self, '_frame_timer'):
            self._frame_timer = 0.0

        self._frame_timer += dt

        if self._frame_timer > delay:
            self._frame_timer = 0.0
            current_index += step
            if current_index >= len(frames):
                current_index = 0
        return current_index