import os
from arcade import *
from arcade import color, key

from random import randint
from time import time

from ball import Ball
from paddle import Player, Enemy


width = 800
height = 600


class PongGame(Window):
    def __init__(self):
        super().__init__(width, height, "PONG")
        set_background_color(color.BLACK)
        # New, and with Sprites
        self.ball = Ball()
        self.player = Player()
        self.enemy = Enemy(width)

        self.paddles = SpriteList()
        self.paddles.append(self.player)
        self.paddles.append(self.enemy)

        self.up_pressed = None
        self.down_pressed = None

        self.state = "MAINMENU"
        self.started_playing = None

        self.player_score = 0
        self.enemy_score = 0
        self.time_left = 0

    def on_draw(self):
        if self.state == "MAINMENU":
            start_render()

            draw_text("PONG", width * 0.5, height * 0.65,
                      color.LIME, font_size=120, anchor_x="center")
            draw_text("Press Space to start".upper(), width * 0.5,
                      height * 0.4, color.WHITE, font_size=20, anchor_x="center")

        if self.state == "PLAYING":
            start_render()

            draw_text(str(self.time_left), width * 0.5, height - 20,
                      color.LIME, font_size=20, anchor_x="center", anchor_y="top")
            draw_text(str(self.player_score), width * 0.4, height * 0.5,
                      color.DIM_GRAY, font_size=40, anchor_x="center", anchor_y="top")
            draw_text(str(self.enemy_score), width * 0.6, height * 0.5,
                      color.DIM_GRAY, font_size=40, anchor_x="center", anchor_y="top")
            for i in range(0, 12, 2):
                draw_line(width * 0.5, height * i / 12, width * 0.5,
                          height * (i + 1) / 12, color.WHITE, line_width=4)

            self.ball.draw()
            self.paddles.draw()

        if self.state == "GAMEOVER":
            start_render()

            draw_text("GAMEOVER", width * 0.5, height * 0.5, color.RED,
                      font_size=120, anchor_x="center", anchor_y="center")

    def on_update(self, delta_time):
        if self.state == "PLAYING":
            # Update the Sprites
            self.ball.update(width, height, self.paddles)
            self.player.update(height)
            self.enemy.update(self.ball, height)

            if self.ball.check_outside(width) == "left":
                self.enemy_score += 1
                self.ball.reset(width, height)
            elif self.ball.check_outside(width) == "right":
                self.player_score += 1
                self.ball.reset(width, height)

            # Keyboard control
            if self.up_pressed:
                self.player.move_up()
            if self.down_pressed:
                self.player.move_down()
            if not self.up_pressed and not self.down_pressed:
                self.player.stop()

            play_time = round(time() - self.started_playing)
            self.time_left = 30 - play_time
            if self.time_left < 0:
                self.state = "GAMEOVER"

    def on_key_press(self, key_pressed, modifiers):
        if self.state == "MAINMENU":
            if key_pressed == key.SPACE:
                self.state = "PLAYING"
                self.started_playing = time()

        if self.state == "PLAYING":
            if key_pressed == key.UP:
                self.up_pressed = True
            if key_pressed == key.DOWN:
                self.down_pressed = True

    def on_key_release(self, key_released, modifiers):
        if self.state == "PLAYING":
            if key_released == key.UP:
                self.up_pressed = False
            if key_released == key.DOWN:
                self.down_pressed = False


# Update the working directory to the correct location of the file
origin = os.path.abspath(__file__)
os.chdir(os.path.dirname(origin))

game = PongGame()

run()
