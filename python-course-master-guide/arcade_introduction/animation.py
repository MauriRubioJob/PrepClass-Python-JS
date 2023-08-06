import arcade


screen_width = 800
screen_height = 600

position_x = 400
position_y = 300

velocity_x = 6
velocity_y = 3


def draw(t):
    global position_x, position_y, velocity_x, velocity_y

    position_x = position_x + velocity_x
    position_y = position_y + velocity_y

    if position_x + 50 > screen_width or position_x - 50 < 0:
        velocity_x = velocity_x * -1

    if position_y + 50 > screen_height or position_y - 50 < 0:
        velocity_y = velocity_y * -1

    arcade.start_render()
    arcade.draw_rectangle_filled(
        position_x, position_y, 100, 100, arcade.color.WHITE)


arcade.open_window(screen_width, screen_height, "Bouncing square")
arcade.set_background_color(arcade.color.ORANGE)
arcade.schedule(draw, 1 / 144)
arcade.run()
