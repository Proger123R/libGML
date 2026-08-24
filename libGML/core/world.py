import pygame
import json
import csv

class World:
    def __init__(self, sc):
        self.sc = sc

    def load_room_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def draw_tile(self, atlas_name, x, y, atlas, width, height):
        wall = atlas.get(atlas_name)
        wallModed = pygame.transform.scale(wall, (width, height))
        self.sc.blit(wallModed, (x, y))

    def load_room_csv(self, filename):
        with open(filename) as f:
            reader = csv.reader(f)
            return list(reader)

    def trigger_tile(self, player_rect, tile_size, map, tile):
        if map is None:
            return None

        col = player_rect.centerx // tile_size
        row = player_rect.centery // tile_size

        rows = len(map)
        if rows == 0:
            return False
        cols = len(map[0])

        if not (0 <= row < rows and 0 <= col < cols):
            return False

        tile_id = map[row][col]
        key = str(tile_id) if isinstance(tile_id, int) else tile_id
        return key == tile

    def draw_layer(self, map, atlas, width, height, camera=None):
        self.map = map
        rows = len(map)
        cols = len(map[0]) if rows > 0 else 0
        for row in range(rows):
            for col in range(cols):
                for i in atlas.keys():
                    if camera:
                        sc_x = (col * width) - camera.x
                        sc_y = (row * height) - camera.y
                    else:
                        sc_x = col * width
                        sc_y = row * height
                    tile = map[row][col]
                    if tile == i:
                        self.draw_tile(i, sc_x, sc_y, atlas, width, height)

    def can_move_to(self, rect, tile_size, blocked_tiles, map):
        corners = [
            (rect.left, rect.top),
            (rect.right - 1, rect.top),
            (rect.left, rect.bottom - 1),
            (rect.right - 1, rect.bottom - 1)
        ]
        for cx, cy in corners:
            mx = int(cx // tile_size)
            my = int(cy // tile_size)
            if not (0 <= my < len(map) and 0 <= mx < len(map[0])):
                return False
            if map[my][mx] in blocked_tiles:
                return False
        return True