import arcade
from WallAwareWalkingSprite import WallAwareWalkingSprite

class AwarePacman(WallAwareWalkingSprite):
    def __init__(self, walls, wall_sprites):
        super().__init__(walls, wall_sprites)
        coords = ((0, 0, 32, 32), (32, 0, 32, 32), (0, 32, 32, 32), (32, 32, 32, 32), (0, 64, 32, 32), (32, 64, 32, 32), (0, 96, 32, 32), (32, 96, 32, 32))
        textures = arcade.load_textures("assets/sheets/pacman.png", coords)
        
        self.walk_right_textures = textures[0:2]
        self.walk_down_textures = textures[2:4]
        self.walk_left_textures = textures[4:6]
        self.walk_up_textures = textures[6:8]
        self.stand_right_textures = textures[0:1]
        self.stand_left_textures = textures[4:5]
        self.texture_change_distance = 25

        self.move_right()
        self.next_direction = None
    
    def update(self):
        
        super().update()

class Pacman(arcade.AnimatedWalkingSprite):
    def __init__(self, scale):
        super().__init__(scale=scale)
        self.scale = scale
        coords = ((0, 0, 32, 32), (32, 0, 32, 32), (0, 32, 32, 32), (32, 32, 32, 32), (0, 64, 32, 32), (32, 64, 32, 32), (0, 96, 32, 32), (32, 96, 32, 32))
        self.textures = arcade.load_textures("assets/sheets/pacman.png", coords)
        
        self.walk_right_textures = self.textures[0:2]
        self.walk_down_textures = self.textures[2:4]
        self.walk_left_textures = self.textures[4:6]
        self.walk_up_textures = self.textures[6:8]
        self.stand_right_textures = self.textures[0:1]
        self.stand_left_textures = self.textures[4:5]

        self.speed = 4
        self.next_direction = None
    
    def update(self, walls):
        if self.next_direction == "up":
            self.center_y += 1
            if not arcade.check_for_collision_with_list(self, walls):
                self.change_y = self.speed
                self.change_x = 0
            self.center_y -= 1
        elif self.next_direction == "left":
            self.center_x -= 1
            if not arcade.check_for_collision_with_list(self, walls):
                self.change_x = -self.speed
                self.change_y = 0
            self.center_x += 1
        elif self.next_direction == "down":
            self.center_y -= 1
            if not arcade.check_for_collision_with_list(self, walls):
                self.change_y = -self.speed
                self.change_x = 0
            self.center_y += 1
        elif self.next_direction == "right":
            self.center_x += 1
            if not arcade.check_for_collision_with_list(self, walls):
                self.change_x = self.speed
                self.change_y = 0
            self.center_x -= 1
        
        self.center_x += self.change_x
        self.center_y += self.change_y