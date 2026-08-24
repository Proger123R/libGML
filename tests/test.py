from libGML.graphics.sprite import Sprite
from libGML.input.keyboard import Keyboard
from libGML.core.world import World
from libGML.graphics.transform import Transform
from libGML.core.camera import Camera
from libGML.core.vector2 import Vector2
import pygame

pygame.init()

sc = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

keyboard = Keyboard()
sprites = Sprite()
world = World(sc)
transform = Transform()
camera = Camera()

speed = 5
texture = sprites.load_texture("player_test.png").convert_alpha()

test = sprites.create_sprite(100, 110, 32, 32)
texture = transform.scale((32, 32), texture)
map = world.load_room_csv("mapL1.csv")
mapL2 = world.load_room_csv("mapL2.csv")

tileset = pygame.image.load("tileset.png").convert_alpha()
atlas = sprites.cutTileSet(tileset, 16, 16)

testiruem = [sprites.load_texture("pl_up.png").convert_alpha(), sprites.load_texture("pl_down.png").convert_alpha(), sprites.load_texture("pl_side.png").convert_alpha()]

blocked_tiles = ['4', '16', '97', '98', '99', '109', '110', '111', '121', '122', '123']

key = 0

while True:
    pygame.event.pump()
    dt = clock.tick(60) / 1000.0

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()

    if keyboard.is_pressed("W"):
        dy = 0
        dy -= speed
        new_test = sprites.move((0, dy), test)
        if world.can_move_to(new_test, 32, blocked_tiles, mapL2):
            test = new_test
    if keyboard.is_pressed("A"):
        dx = 0
        dx -= speed
        new_test = sprites.move((dx, 0), test)
        if world.can_move_to(new_test, 32, blocked_tiles, mapL2):
            test = new_test
    if keyboard.is_pressed("S"):
        dy = 0
        dy += speed
        new_test = sprites.move((0, dy), test)
        if world.can_move_to(new_test, 32, blocked_tiles, mapL2):
            test = new_test
    if keyboard.is_pressed("D"):
        dx = 0
        dx += speed
        new_test = sprites.move((dx, 0), test)
        if world.can_move_to(new_test, 32, blocked_tiles, mapL2):
            test = new_test

    sc.fill((20, 20, 30))

    camera.follow(test, sc)

    world.draw_layer(map, atlas, 32, 32, camera)
    world.draw_layer(mapL2, atlas, 32, 32, camera)

    key = sprites.get_frame(testiruem, key, dt, delay=0.5)
    texture = testiruem[key]

    sprites.draw(sc, test, texture, camera)

    clock.tick(60)
    pygame.display.set_caption(str(clock.get_fps()))
    pygame.display.flip()