libGML Documentation — Version 0.2

This document covers the current release of libGML (Game Making Library), version 0.2.
Features implemented

    Sprite handling — creation, movement, and rendering.

    Keyboard input — is_pressed(key) method, e.g. is_pressed("W").

    World rendering — load maps from JSON. CSV support will be added in future versions.

    Transform — scaling and rotation utilities.

    Camera2D — follow the player with a camera.

    Animation — simple frame-based animation system.

    Vector2 — optional vector math for movement and calculations.

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
Loading a map from JSON

Load your map from a JSON file using World.load_room(). No specific schema is required — just access your map via map['your_key'].
Texture atlas

Create a dictionary (atlas) that maps tile IDs to loaded surfaces.

    ⚠️ Important: The keys in your atlas must match the tile numbers used in your map. For example, if your map contains 11, then your atlas must have a key "11". If they don't match, textures will be drawn incorrectly.

Collisions

Create a list of tile IDs that act as obstacles:
python

blocked_tiles = ["11", "9", "10", "8"]

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

    Check collision with can_move_to(new_test, tile_size, blocked_tiles, map['map']).

        It returns True if movement is allowed, False otherwise.

    If True, assign test = new_test.

Repeat this logic for the A, S, and D keys.
NEW: Camera2D

The camera follows the player and adjusts the view.
python

camera = Camera()
camera.follow(player_rect, screen)

When drawing the world or sprites, simply pass the camera as an argument:
python

world.draw_layer(map["map"], atlas, tile_width, tile_height, camera)
sprites.draw(screen, rect, texture, camera)

NEW: Animation

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

NEW: Vector2 (optional)

Vector2 is available for users who prefer vector-based movement and math.
python

from libGML.core.vector2 import Vector2

pos = Vector2(100, 200)
pos += Vector2(5, 0) * dt

This class includes:

    Addition, subtraction, multiplication, division

    Length, normalisation, distance

Rendering

    Fill the screen with screen.fill().

    Draw the world using world.draw_layer(map['map'], atlas, tile_width, tile_height, camera).

    Draw the player with sprites.draw(screen, rect, texture, camera).

Everything else works as you'd expect in standard Pygame.

Thank you for reading! I hope libGML makes your game development easier and more enjoyable.

— ImPulseStory
