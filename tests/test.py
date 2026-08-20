from libGML.graphics.sprite import Sprite
from libGML.input.keyboard import Keyboard
from libGML.core.world import World
from libGML.graphics.transform import Transform
import pygame

pygame.init()

sc = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

keyboard = Keyboard()
sprites = Sprite()
world = World(sc)
transform = Transform()

speed = 5
texture = sprites.load_texture("player_test.png").convert_alpha()

test = sprites.create_sprite(100, 110, 32, 32, texture)
texture = transform.scale((32, 32), texture)
map = world.load_room("roomTest.json")

atlas = {
        "9": pygame.image.load("assets/walleft.png").convert_alpha(),
        "10": pygame.image.load("assets/wallford.png").convert_alpha(),
        "12": pygame.image.load("assets/spawn.png").convert_alpha(),
        "11": pygame.image.load("assets/cube_test.png").convert_alpha(),
        "1": pygame.image.load("assets/map-tiles/g1.png").convert_alpha(),
        "2": pygame.image.load("assets/map-tiles/g2.png").convert_alpha(),
        "3": pygame.image.load("assets/map-tiles/g3.png").convert_alpha(),
        "4": pygame.image.load("assets/map-tiles/g4.png").convert_alpha(),
        "5": pygame.image.load("assets/map-tiles/g5.png").convert_alpha(),
        "6": pygame.image.load("assets/map-tiles/g6.png").convert_alpha(),
        "7": pygame.image.load("assets/map-tiles/g7.png").convert_alpha(),
        "8": pygame.image.load("assets/walback.png").convert_alpha(),
                    }

blocked_tiles = ["11", "9", "10", "8"]

while True:
    pygame.event.pump()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()

    if keyboard.is_pressed("W"):
        dy = 0
        dy -= speed
        new_test = sprites.move((0, dy), test)
        if world.can_move_to(new_test, 32, blocked_tiles, map['map']):
            test = new_test
    if keyboard.is_pressed("A"):
        dx = 0
        dx -= speed
        new_test = sprites.move((dx, 0), test)
        if world.can_move_to(new_test, 32, blocked_tiles, map['map']):
            test = new_test
    if keyboard.is_pressed("S"):
        dy = 0
        dy += speed
        new_test = sprites.move((0, dy), test)
        if world.can_move_to(new_test, 32, blocked_tiles, map['map']):
            test = new_test
    if keyboard.is_pressed("D"):
        dx = 0
        dx += speed
        new_test = sprites.move((dx, 0), test)
        if world.can_move_to(new_test, 32, blocked_tiles, map['map']):
            test = new_test

    sc.fill((20, 20, 30))
    world.draw_layer(map["map"], atlas, 32, 32)

    sprites.draw(sc, test, texture)

    clock.tick(60)
    pygame.display.set_caption(str(clock.get_fps()))
    pygame.display.flip()