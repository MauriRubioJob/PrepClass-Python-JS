import arcade
from directions import Direction

class Pacman(arcade.AnimatedWalkingSprite):
    def __init__(self, scale, walls):
        super().__init__()
        coordinates = [[x * 32 * scale, y * 32 * scale, 32 * scale, 32 * scale] for y in range(4) for x in range(10, 12)]
        textures = arcade.load_textures(f"assets/actors{'_2x' if scale == 2 else ''}.png", coordinates)
        self.walk_right_textures = textures[0:2]
        self.walk_down_textures = textures[2:4]
        self.walk_left_textures = textures[4:6]
        self.walk_up_textures = textures[6:8]
        self.stand_right_textures = textures[0:1]
        self.stand_left_textures = textures[4:5]

        self.speed = 2 * scale
        self.texture_change_distance = 12 * scale

        self.direction = None
        self.next_direction = None

        self.walls = walls

        self.update_animation()
    
    def update(self):
        i = int(self.center_x // self.texture.width)
        j = int(self.center_y // self.texture.height)

        if self.top % self.width == 0 and self.right % self.height == 0:
            # if movement possible
            walls = {
                Direction.UP: self.walls[j + 1][i] == 1,
                Direction.RIGHT: self.walls[j][i + 1] == 1,
                Direction.DOWN: self.walls[j - 1][i] == 1,
                Direction.LEFT: self.walls[j][i - 1] == 1
            }
            if self.next_direction and not walls[self.next_direction]:
                self.direction = self.next_direction
        
            if self.direction and walls[self.direction] and (self.center_x == (i + 0.5) * self.width or self.center_y == (j + 0.5) * self.height):
                self.direction = None
        
        if self.direction and self.next_direction and abs(self.next_direction.value - self.direction.value) == 2:
            self.direction = self.next_direction

        self.change_x = 0
        self.change_y = 0
        if self.direction == Direction.UP:
            self.change_y = self.speed
        elif self.direction == Direction.RIGHT:
            self.change_x = self.speed
        elif self.direction == Direction.DOWN:
            self.change_y = -self.speed
        elif self.direction == Direction.LEFT:
            self.change_x = -self.speed
        
        self.center_x += self.change_x
        self.center_y += self.change_y
        
    
    def move_up(self):
        self.next_direction = Direction.UP
    

    def move_right(self):
        self.next_direction = Direction.RIGHT
    

    def move_down(self):
        self.next_direction = Direction.DOWN
    

    def move_left(self):
        self.next_direction = Direction.LEFT
        
