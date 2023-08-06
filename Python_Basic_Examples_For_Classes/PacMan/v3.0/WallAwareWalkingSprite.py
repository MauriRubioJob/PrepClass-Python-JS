import arcade
from random import choice

RIGHT = 1
UP = 2
LEFT = 3
DOWN = 4

class WallAwareWalkingSprite(arcade.AnimatedWalkingSprite):
    def __init__(self, walls, wall_sprites):
        super().__init__()
        self.direction = None
        self.next_direction = None
        self.speed = 4

        self.walls = {
            "positions": walls,
            "sprites": wall_sprites,
            "length": len(walls),
            "size": wall_sprites[0].width if len(wall_sprites) else None
        }

        # self.walls = walls
        # self.wall_sprites = wall_sprites
        # self.walls_length = len(walls)
        # self.wall_size = wall_sprites[0].width if len(wall_sprites) else None
    
    def walk(self):
        if self.top % 64 == 0 and self.left % 64 == 0:
            # i = self.center_x // self.wall_size
            # j = self.center_y // self.wall_size
            i = self.center_x // self.walls["size"]
            j = self.center_y // self.walls["size"]
            
            print("center_x: {} center_y: {}".format(self.center_x, self.center_y))
            print("i: {} j: {}".format(i, j))

            if not self.direction == self.next_direction:
            
            spaces = []
            if i < self.walls_length - 1 and j < self.walls_length and not self.walls[j][i + 1]:
                spaces.append(RIGHT)
            if j > 0 and i < self.walls_length and not self.walls[j - 1][i]:
                spaces.append(UP)
            if i > 0 and j < self.walls_length and not self.walls[j][i - 1]:
                spaces.append(LEFT)
            if j < self.walls_length - 1 and i < self.walls_length and not self.walls[j + 1][i]:
                spaces.append(DOWN)

            spaces = [
                RIGHT if i < self.walls["length"] - 1 and j < self.walls["length"] and not self.walls["positions"][j][i + 1] else False,
                UP if j > 0 and i < self.walls["length"] and not self.walls["positions"][j - 1][i] else False
            ]
            
            if len(spaces) > 2 or not spaces.count(self.direction):
                self.direction = choice(spaces)

        if self.direction == RIGHT:
            self.center_x += self.speed
        elif self.direction == LEFT:
            self.center_x -= self.speed
        elif self.direction == UP:
            self.center_y -= self.speed
        elif self.direction == DOWN:
            self.center_y += self.speed
    
    def move_right(self):
        self.direction = RIGHT
    
    def move_left(self):
        self.direction = LEFT
    
    def move_up(self):
        self.direction = UP
    
    def move_down(self):
        self.direction = DOWN
    
    def update(self):
        self.walk()
