libGML Documentation — Version 0.3

This document covers the current release of libGML (Game Making Library), version 0.3.
Features implemented

    Sprite handling — creation, movement, and rendering.

    Keyboard input — is_pressed(key) method, e.g. is_pressed("W").

    World rendering — load maps from JSON or CSV.

    Transform — scaling and rotation utilities.

    Camera2D — follow the player with a camera.

    Animation — simple frame-based animation system.

    Vector2 — optional vector math for movement and calculations.

    TileSet support — load and cut tile sheets into individual tiles.

    Room transitions — switch between maps using triggers.

Getting started

Open test.py in a second window for reference.

At the top of the file, we import all required libraries, including Pygame (libGML does not hide Pygame — you can still use it directly).

Then we:

    initialise Pygame,

    create a game window,

    create a Clock() object,

    and instantiate the libGML classes. These are required.

After that, we load textures and set a movement speed.
Creating a sprite

Use the create_sprite(x, y, width, height, texture) method. This returns a standard Pygame Rect object, so store it in a variable.

Then you can scale the sprite using Transform.scale().
Loading a map
From JSON
python

map_data = world.load_room("map.json")

No specific schema is required — just access your map via map['your_key'].
From CSV (NEW in 0.3)
python

map_data = world.load_room_csv("map.csv")

The CSV file should contain numbers separated by commas, where each number corresponds to a tile index in your tileset.
TileSet (NEW in 0.3)

Load a tileset image and cut it into individual tiles:
python

tileset = pygame.image.load("tileset.png").convert_alpha()
tiles = sprites.cutTileSet(tileset, tile_width, tile_height)

This returns a list of surfaces, where the index is the tile ID.

You can then use this list in draw_layer:
python

world.draw_layer(map_data, tiles, tile_width, tile_height, camera)

    ⚠️ Important: cutTileSet returns a list where the index corresponds to the tile ID. If your CSV file contains strings, convert them to integers before using them as indices.

Collisions

Create a list of tile IDs that act as obstacles:
python

blocked_tiles = ['5', '16', '97', '98', '99', '109', '110', '111', '121', '122', '123']

    ⚠️ Important: The tile IDs in blocked_tiles must match the format used in your map. If your map contains strings (e.g., from a CSV file), use strings in blocked_tiles. Use single quotes to avoid type mismatches.

The main loop

Start your game loop as usual.

    ⚠️ Important: Always call pygame.event.pump() at the start of each frame. Without it, the game will lag or freeze.

Add the standard quit handler.
Movement and collisions — step by step

We’ll use the W key as an example:

    Check if "W" is pressed.

    Set dy = 0, then subtract speed from it (dy -= speed).

    Create a new rectangle (new_test) by calling move((0, dy), test). This moves the rectangle vertically.

        Note: move() returns a new rectangle; the original remains unchanged. This is important for collision detection.

    Check collision with can_move_to(new_test, tile_size, blocked_tiles, map_data).

        It returns True if movement is allowed, False otherwise.

    If True, assign test = new_test.

Repeat this logic for the A, S, and D keys.
Camera2D

The camera follows the player and adjusts the view.
python

camera = Camera()
camera.follow(player_rect, screen)

When drawing the world or sprites, simply pass the camera as an argument:
python

world.draw_layer(map_data, tiles, tile_width, tile_height, camera)
sprites.draw(screen, rect, texture, camera)

Animation

libGML provides a simple frame animation system.
python

frames = [surface1, surface2, surface3]
index = 0

# In the game loop:
index, texture = sprites.get_frame(frames, index, dt, delay=0.1)

    frames — a list of surfaces.

    index — current frame index.

    dt — delta time (use clock.tick(60) / 1000.0).

    delay — time in seconds between frames.

Vector2 (optional)

Vector2 is available for users who prefer vector-based movement and math.
python

from libGML.core.vector2 import Vector2

pos = Vector2(100, 200)
pos += Vector2(5, 0) * dt

This class includes:

    Addition, subtraction, multiplication, division

    Length, normalisation, distance

Room transitions (NEW in 0.3)

You can switch between rooms using trigger_room:
python

if world.trigger_room(player_rect, tile_size, map_data, trigger_tile_id):
    current_room += 1

This method checks if the player is standing on a specific tile and returns True or False.
Rendering

    Fill the screen with screen.fill().

    Draw the world using world.draw_layer(map_data, tiles, tile_width, tile_height, camera).

    Draw the player with sprites.draw(screen, rect, texture, camera).

Everything else works as you'd expect in standard Pygame.

Thank you for reading! I hope libGML makes your game development easier and more enjoyable.

— ImPulseStory
