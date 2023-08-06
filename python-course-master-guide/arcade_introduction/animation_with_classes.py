import arcade


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Bouncing square", update_rate=1/144)
        arcade.set_background_color(arcade.color.ORANGE)

        self.position_x = 400
        self.position_y = 300

        self.velocity_x = 6
        self.velocity_y = 3

    def on_update(self, delta_time):
        self.position_x = self.position_x + self.velocity_x
        self.position_y = self.position_y + self.velocity_y

        if self.position_x + 50 > self.width or self.position_x - 50 < 0:
            self.velocity_x = self.velocity_x * -1

        if self.position_y + 50 > self.height or self.position_y - 50 < 0:
            self.velocity_y = self.velocity_y * -1

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(
            self.position_x, self.position_y, 100, 100, arcade.color.WHITE)


window = Window()
arcade.run()
