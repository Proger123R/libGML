import pygame
import json

class World:
    def __init__(self, sc):
        self.sc = sc

    def load_room(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def draw_tile(self, atlas_name, x, y, atlas, width, height):
        wall = atlas.get(atlas_name)
        wallModed = pygame.transform.scale(wall, (width, height))
        self.sc.blit(wallModed, (x, y))

    #def trigger_room(self, player_rect):
    #    if self.map_l2 is None:
    #        return None

    #    col = player_rect.centerx // BrickWallX
    #    row = player_rect.centery // BrickWallX

    #    rows = len(self.map_l2)
    #    if rows == 0:
    #        return False
    #    cols = len(self.map_l2[0])

    #    if not (0 <= row < rows and 0 <= col < cols):
    #        return False

    #    tile_id = self.map_l2[row][col]
    #    key = str(tile_id) if isinstance(tile_id, int) else tile_id
    #    return key == "13"

    def draw_layer(self, map, atlas, width, height):
        self.map = map
        rows = len(map)
        cols = len(map[0]) if rows > 0 else 0
        for row in range(rows):
            for col in range(cols):
                for i in atlas.keys():
                    tile = map[row][col]
                    x = col * width
                    y = row * height
                    if tile == i:
                        self.draw_tile(i, x, y, atlas, width, height)

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