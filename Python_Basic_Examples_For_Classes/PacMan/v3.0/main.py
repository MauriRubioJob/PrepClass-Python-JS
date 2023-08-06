import arcade
from Pacman import Pacman, AwarePacman
from Wall import Wall

class Game(arcade.Window):
    def __init__(self, size, scale):
        super().__init__(32 * size * scale, 32 * size * scale, "Pacman")
        self.size = size
        self.scale = scale

        self.setup()
    
    def setup(self):
        self.state = "DRAWING"
        
        Wall.load_textures(self.scale)
        Wall.edged = False
        self.wall_positions = [[False for i in range(self.size)] for j in range(self.size)]
        self.walls = arcade.SpriteList()

        self.pacman = Pacman(self.scale)
        self.pacman.center_x = self.width / 2
        self.pacman.center_y = self.height / 2

    
    def on_update(self, delta):
        if self.state == "DRAWING":
            pass
        elif self.state == "PLAYING":
        #     self.pacman.update()
        #     self.pacman.update_animation()
            self.aware_pacman.walk()
            self.aware_pacman.update_animation()
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.state, 0, 0, arcade.color.WHITE)
        if self.state == "DRAWING":
            self.walls.draw()
        elif self.state == "PLAYING":
            self.walls.draw()
        #     self.pacman.draw()
            self.aware_pacman.draw()
   
    def create_walls(self):
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
        if self.state == "DRAWING":
            if symbol == arcade.key.SPACE:
                self.aware_pacman = AwarePacman(self.wall_positions, self.walls)
                self.state = "PLAYING"
        elif self.state == "PLAYING":
            if [arcade.key.RIGHT, arcade.key.D].count(symbol):
                self.aware_pacman.move_right()
            elif [arcade.key.LEFT, arcade.key.A].count(symbol):
                self.aware_pacman.move_left()
            elif [arcade.key.UP, arcade.key.W].count(symbol):
                self.aware_pacman.move_down()
            elif [arcade.key.DOWN, arcade.key.S].count(symbol):
                self.aware_pacman.move_up()

def main():
    game = Game(21, 1)
    arcade.run()

if __name__ == "__main__":
    main()
