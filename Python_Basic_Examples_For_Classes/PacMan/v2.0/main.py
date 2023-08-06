import arcade
from Wall import Wall
 
class Window(arcade.Window):
    def __init__(self, size, scale=1):
        dimension = size * scale * 32
        super().__init__(dimension, dimension, "Continuous Wall Sprites")
        self.size = size
        self.scale = scale
        self.setup()
   
    def setup(self):
        Wall.load_textures(self.scale)
        Wall.edged = False
 
        self.wall_positions = [[False for i in range(self.size)] for j in range(self.size)]
 
        self.walls = arcade.SpriteList()
   
    def on_update(self, delta):
        None
   
    def on_draw(self):
        arcade.start_render()
        self.walls.draw()
   
    def create_walls(self):
        del self.walls
        self.walls = arcade.SpriteList()
        for j in range(self.size):
            for i in range(self.size):
                if self.wall_positions[j][i]:
                    self.walls.append(Wall(self.wall_positions, i, j))
   
    def set_wall(self, x, y):
        if not self.walls_changed[y][x]:
            self.walls_changed[y][x] = True
            self.wall_positions[y][x] = self.wall_setting
            self.create_walls()
   
    def on_mouse_press(self, x, y, button, modifiers):
        self.walls_changed = [[False for i in range(self.size)] for j in range(self.size)]
        self.wall_setting = button == arcade.MOUSE_BUTTON_LEFT
        self.set_wall(x // (self.scale * 32), y // (self.scale * 32))
   
    def on_mouse_release(self, x, y, button, modifiers):
        self.walls_changed = None
   
    def on_mouse_drag(self, mouse_x, mouse_y, dx, dy, buttons, modifiers):
        if mouse_x > 0 and mouse_x < self.width and mouse_y > 0 and mouse_y < self.width:
            self.set_wall(mouse_x // (self.scale * 32), mouse_y // (self.scale * 32))
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            print(self.wall_positions)
 
window = Window(11, 2)
arcade.run()