import arcade
from Player import Player
from Wall import Wall
from Ghost import Ghost

class Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(64 * width, 64 * height, "Pac-Man")
        self.dimension = 64
        self.scale = 2
    
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

        self.wall_positions = [
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 2, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1]
        ]

        self.walls = arcade.SpriteList(is_static=True)
        self.dots = arcade.SpriteList()
        self.create_walls()
        
        self.sound_beginning = arcade.load_sound("assets/audio/beginning.ogg")
        self.sound_moving = arcade.load_sound("assets/audio/chomp.mp3")
        self.sound_moving_playing = False

        self.state = "LOADING"
        self.loading_time = 1    
    def on_update(self, delta):
        self.frames += 1
        self.time += delta
        # print("{} {} {}".format(self.frames, round(self.time, 4), round(delta, 4) * 1000))
        if self.state == "LOADING" and self.time > self.loading_time:
            self.state = "COUNTDOWN"
            self.time = 0
            self.frames = 0

        if self.state == "COUNTDOWN" or self.state == "PLAYING":

            if self.frames == 1:
                print("Playing beginning")
                # arcade.play_sound(self.sound_beginning)
            
            if self.state == "COUNTDOWN" and self.time > 4:
                self.state = "PLAYING"
            
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
                if dot.big:
                    for ghost in self.ghosts:
                        ghost.make_vulnerable()
                dot.kill()
            
            collided_ghosts = arcade.check_for_collision_with_list(self.player, self.ghosts)
            for ghost in collided_ghosts:
                if ghost.vulnerable:
                    pass
                else:
                    arcade.close_window()
            
            if self.state == "PLAYING" and len(self.dots) == 0:
                for wall in self.walls:
                    wall.kill()
   
    def create_walls(self):
        for i in range(len(self.wall_positions)):
            for j in range(len(self.wall_positions[i])):
                if self.wall_positions[i][j] == 0:
                    dot = arcade.Sprite(filename="assets/dot_9.png", scale=1, center_x=(j + 0.5) * self.scale * 32, center_y=(i + 0.5) * self.scale * 32)
                    dot.big = False
                    self.dots.append(dot)
                
                if self.wall_positions[i][j] == 1:
                    self.walls.append(Wall(self.wall_positions, j, i))
                
                if self.wall_positions[i][j] == 2:
                    dot = arcade.Sprite(filename="assets/dot_18.png", scale=1, center_x=(j + 0.5) * self.scale * 32, center_y=(i + 0.5) * self.scale * 32)
                    dot.big = True
                    self.dots.append(dot)
        
    def on_draw(self):
        arcade.start_render()
        if self.state == "COUNTDOWN" or self.state == "PLAYING":
            self.player.draw()
            self.walls.draw()
            self.dots.draw()
            self.ghosts.draw()
            
        if self.state == "COUNTDOWN":
            arcade.draw_rectangle_filled(self.width / 2, self.height / 2, self.width, self.height, (0, 0, 0, 100))
            # arcade.draw_text("{}".format("Ready!" if self.time > 3 else round(3 - self.time)), self.width / 2, self.height / 2, arcade.color.YELLOW, font_size=200, font_name="Impact", anchor_x="center", anchor_y="center", width=self.width, align="center")
            
    def on_key_press(self, symbol, modifiers):
        if self.state == "PLAYING":
            if symbol == arcade.key.W or symbol == arcade.key.UP:
                self.player.next_direction = "up"
            elif symbol == arcade.key.A or symbol == arcade.key.LEFT:
                self.player.next_direction = "left"
            elif symbol == arcade.key.S or symbol == arcade.key.DOWN:
                self.player.next_direction = "down"
            elif symbol == arcade.key.D or symbol == arcade.key.RIGHT:
                self.player.next_direction = "right"


def main():
    window = Window(17, 11)
    window.setup()
    arcade.run()

main()
