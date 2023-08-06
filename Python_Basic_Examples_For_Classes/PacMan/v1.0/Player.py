import arcade

class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__(scale=2)
        self.walk_down_textures = [
            arcade.load_texture("assets/pacman_down_0.png"),
            arcade.load_texture("assets/pacman_down_1.png")
        ]
        self.walk_up_textures = [
            arcade.load_texture("assets/pacman_up_0.png"),
            arcade.load_texture("assets/pacman_up_1.png")
        ]
        self.walk_left_textures = [
            arcade.load_texture("assets/pacman_left_0.png"),
            arcade.load_texture("assets/pacman_left_1.png")
        ]
        self.walk_right_textures = [
            arcade.load_texture("assets/pacman_right_0.png"),
            arcade.load_texture("assets/pacman_right_1.png")
        ]
        self.stand_left_textures = [self.walk_left_textures[0]]
        self.stand_right_textures = [self.walk_right_textures[0]]
        self.texture = self.walk_right_textures[0]

        self.texture_change_distance = 25
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