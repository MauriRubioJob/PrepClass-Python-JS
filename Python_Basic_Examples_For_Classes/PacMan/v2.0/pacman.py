import arcade
from Player import Player
from Wall import Wall
from Ghost import Ghost

class Window(arcade.Window):
    def __init__(self, dimension, scale):
        super().__init__(32 * dimension * scale, 32 * dimension * scale, "Pac-Man")
        self.dimension = dimension
        self.scale = scale
    
    def setup(self):
        Wall.load_textures(self.scale)
        self.frames = 0
        self.time = 0

        self.player = Player(self.scale)
        self.player.center_x = self.width / 2
        self.player.center_y = self.height / 2

        self.ghost_cyan = Ghost(self.scale, self.dimension, colour="cyan")
        self.ghost_red = Ghost(self.scale, self.dimension, colour="red")
        self.ghost_pink = Ghost(self.scale, self.dimension, colour="pink")
        self.ghost_orange = Ghost(self.scale, self.dimension, colour="orange")

        self.ghosts = arcade.SpriteList()
        self.ghosts.append(self.ghost_cyan)
        self.ghosts.append(self.ghost_red)
        self.ghosts.append(self.ghost_pink)
        self.ghosts.append(self.ghost_orange)

        self.wall_positions = [[True, False, True, True, True, True, True, True, True, False, True], [False, False, False, False, False, False, False, False, False, False, False], [True, False, True, True, True, True, True, True, True, False, True], [True, False, True, False, False, False, False, False, True, False, True], [True, False, True, False, True, False, True, False, True, False, True], [True, False, True, False, True, False, True, False, True, False, True], [True, False, True, False, True, True, True, False, True, False, True], [True, False, True, False, False, False, False, False, True, False, True], [True, False, True, True, True, False, True, True, True, False, True], [False, False, False, False, False, False, False, False, False, False, False], [True, False, True, True, True, True, True, True, True, False, True]]
        self.wall_positions = [[False for i in range(self.dimension)] for j in range(self.dimension)]

        self.walls = arcade.SpriteList()
        self.dots = arcade.SpriteList()
        
        self.sound_beginning = arcade.load_sound("assets/audio/beginning.mp3")
        self.sound_moving = arcade.load_sound("assets/audio/chomp.mp3")
        self.sound_moving_playing = False

        self.state = "DRAWING"



        
    
    def on_update(self, delta):

        if self.state == "COUNTDOWN" or self.state == "PLAYING":
            self.frames += 1
            self.time += delta
            
            if self.state == "COUNTDOWN" and self.time > 4:
                self.state = "PLAYING"

            if self.frames == 1:
                arcade.play_sound(self.sound_beginning)
            
            if self.state == "PLAYING":
                for ghost in self.ghosts:
                    ghost.update(self.width, self.height, self.walls, self.wall_positions)
            for ghost in self.ghosts:
                ghost.update_animation()
            
            if (not self.player.change_x == 0 or not self.player.change_y == 0) and not self.sound_moving_playing:
                arcade.play_sound(self.sound_moving)
                self.sound_moving_playing = 0.6
            
            if self.sound_moving_playing > 0:
                self.sound_moving_playing -= delta
            if self.sound_moving_playing < 0:
                self.sound_moving_playing = False

            self.player.update(self.walls)
            self.player.update_animation()

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

            collided_dots = arcade.check_for_collision_with_list(self.player, self.dots)
            for dot in collided_dots:
                dot.kill()
            
            if arcade.check_for_collision_with_list(self.player, self.ghosts):
                pass
                # arcade.close_window()
            
            if len(self.dots) == 0:
                for wall in self.walls:
                    wall.kill()
   
    def create_walls(self):
        self.walls = arcade.SpriteList()
        for j in range(self.dimension):
            for i in range(self.dimension):
                if self.wall_positions[j][i]:
                    self.walls.append(Wall(self.wall_positions, i, j))
   
    def set_wall(self, x, y):
        if not self.walls_changed[y][x]:
            print("Setting wall {} {}".format(x, y))
            self.walls_changed[y][x] = True
            self.wall_positions[y][x] = self.wall_setting
            self.create_walls()
   
    def on_mouse_press(self, x, y, button, modifiers):
        if self.state == "DRAWING":
            self.walls_changed = [[False for i in range(self.dimension)] for j in range(self.dimension)]
            self.wall_setting = button == arcade.MOUSE_BUTTON_LEFT
            self.set_wall(x // (self.scale * 32), y // (self.scale * 32))
    
    
    def on_mouse_release(self, x, y, button, modifiers):
        if self.state == "DRAWING":
            self.walls_changed = None
   

    def on_mouse_drag(self, mouse_x, mouse_y, dx, dy, buttons, modifiers):
        if self.state == "DRAWING":
            if mouse_x > 0 and mouse_x < self.width and mouse_y > 0 and mouse_y < self.width:
                self.set_wall(mouse_x // (self.scale * 32), mouse_y // (self.scale * 32))
    
    
    def on_draw(self):
        arcade.start_render()
        if self.state == "COUNTDOWN" or self.state == "PLAYING":
            self.player.draw()
            self.walls.draw()
            self.dots.draw()
            self.ghosts.draw()
            
        if self.state == "COUNTDOWN":
            arcade.draw_rectangle_filled(self.width / 2, self.height / 2, self.width, self.height, (0, 0, 0, 100))
            arcade.draw_text("READY!", self.width / 2, self.height / 2, arcade.color.YELLOW, font_size=100, font_name="Impact", anchor_x="center", anchor_y="center", width=10000, align="center")
        elif self.state == "DRAWING":
            self.walls.draw()
    
    def on_key_press(self, symbol, modifiers):
        if self.state == "DRAWING":
            if symbol == arcade.key.SPACE:
                self.state = "COUNTDOWN"

                for i in range(len(self.wall_positions)):
                    for j in range(len(self.wall_positions[i])):
                        if self.wall_positions[i][j]:
                            self.walls.append(Wall(self.wall_positions, j, i))
                        
                        if self.wall_positions[i][j] == False:
                            dot = arcade.Sprite(filename="assets/dot_9.png", scale=1, center_x=(j + 0.5) * self.scale * 32, center_y=(i + 0.5) * self.scale * 32)
                            self.dots.append(dot)
        elif self.state == "PLAYING":
            if symbol == arcade.key.W or symbol == arcade.key.UP:
                self.player.next_direction = "up"
            elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
                self.player.next_direction = "left"
            elif symbol == arcade.key.S or symbol == arcade.key.DOWN:
                self.player.next_direction = "down"
            elif symbol == arcade.key.D or symbol == arcade.key.RIGHT:
                self.player.next_direction = "right"


def main():
    window = Window(11, 2)
    window.setup()
    arcade.run()
main()
