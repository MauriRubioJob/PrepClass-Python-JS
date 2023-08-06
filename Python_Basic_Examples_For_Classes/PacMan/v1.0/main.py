import arcade
from Player import Player
from Wall import Wall

class Window(arcade.Window):
    def __init__(self):
        super().__init__(640, 640, "Pac-Man")
    
    def setup(self):
        self.frames = 0
        self.time = 0

        self.player = Player()
        self.player.center_x = self.width / 2
        self.player.center_y = self.height / 2

        self.wall_positions = [[False for i in range(10)] for j in range(10)]

        self.walls = arcade.SpriteList()

        for i in range(len(self.wall_positions)):
            for j in range(len(self.wall_positions[i])):
                if self.wall_positions[i][j]:
                    self.walls.append(Wall(self.wall_positions, j, i))
        
        self.ghost_textures = arcade.load_textures("assets/sheets/actors.png", ((0, 0, 32, 32), (32, 0, 32, 32), (0, 32, 32, 32), (32, 32, 32, 32), (0, 64, 32, 32), (32, 64, 32, 32), (0, 96, 32, 32), (32, 96, 32, 32)), scale=2)

        self.ghost1 = arcade.Sprite("assets/sheets/actors.png", scale=2, image_x=0, image_y=0, image_width=32, image_height=32, center_x=100, center_y=100)
        self.ghost_animated = arcade.AnimatedTimeSprite(center_x=200, center_y=100)
        self.ghost_animated.textures = self.ghost_textures
        
    
    def on_update(self, delta):
        self.frames += 1
        self.time += delta

        self.player.update(self.walls)
        self.player.update_animation()
        self.ghost_animated.update_animation()

        if self.player.left > self.width:
            self.player.right = 0
        if self.player.right < 0:
            self.player.left = self.width

        if self.player.bottom > self.height:
            self.player.top = 0
        if self.player.top < 0:
            self.player.bottom = self.height
        
        if arcade.check_for_collision_with_list(self.player, self.walls):
            self.player.center_x -= self.player.change_x
            self.player.center_y -= self.player.change_y
            self.player.change_x = 0
            self.player.change_y = 0

    
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.walls.draw()
        self.ghost1.draw()
        self.ghost_animated.draw()
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player.next_direction = "up"
        elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.next_direction = "left"
        elif symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.player.next_direction = "down"
        elif symbol == arcade.key.D or symbol == arcade.key.RIGHT:
            self.player.next_direction = "right"

    
window = Window()
window.setup()
arcade.run()
