from libGML.graphics import sprite
import pygame

pygame.init()

sprite = sprite.Sprite()

sc = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

tileset = pygame.image.load("tileset.png").convert_alpha()

tiles = sprite.cutTileSet(tileset, 16, 16)
print(tiles)