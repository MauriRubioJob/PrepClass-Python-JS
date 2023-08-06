from random import choice

import arcade

import arcade_monkeypatch
from wall import Wall
from pacman import Pacman


class Window(arcade.Window):
    def __init__(self, rows, columns, scale):
        super().__init__(32 * rows * scale, 32 * columns * scale, "Pacman")
        self.rows = rows
        self.cols = columns
        self.scale = scale


    def setup(self):
        self.frames = 0
        self.time = 0
        self.create_random_walls()
        self.pacman = Pacman(self.scale, self.grid)
        self.actors = arcade.SpriteList()
        self.actors.append(self.pacman)

        self.pacman.set_position(32 * 8.5 * self.scale, 32 * 8.5 * self.scale)


    def on_update(self, delta):
        self.frames += 1
        self.time += delta

        self.actors.update()
        self.actors.update_animation()

        if self.pacman.left > self.width:
            self.pacman.right = 0
        elif self.pacman.right < 0:
            self.pacman.left = self.width
    

    def on_draw(self):
        arcade.start_render()

        self.wall_sprites.draw()
        self.actors.draw()
    

    def create_walls(self):
        self.wall_sprites = arcade.SpriteList(is_static=True)
        for y, row in enumerate(self.grid):
            for x, item in enumerate(row):
                if item == 1:
                    self.wall_sprites.append(Wall(self.grid, x, y, self.scale))
    

    def create_random_walls(self):
        from random import randint
        self.grid = [[randint(1, 5) for x in range(self.rows)] for y in range(self.cols)]
        self.create_walls()
    

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.create_random_walls()
            self.pacman.walls = self.grid
        elif symbol == arcade.key.W:
            self.pacman.move_up()
        elif symbol == arcade.key.A:
            self.pacman.move_left()
        elif symbol == arcade.key.S:
            self.pacman.move_down()
        elif symbol == arcade.key.D:
            self.pacman.move_right()
    


if __name__ == "__main__":
    window = Window(18, 18, 1)
    window.setup()
    arcade.run()
