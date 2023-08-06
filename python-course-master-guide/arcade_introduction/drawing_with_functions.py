import arcade

screen_width = 800
screen_height = 600


def draw_background():
    arcade.draw_lrtb_rectangle_filled(
        0, screen_width, screen_height, screen_height / 3,
        arcade.color.SKY_BLUE)
    arcade.draw_lrtb_rectangle_filled(
        0, screen_width, screen_height / 3, 0,
        arcade.color.DARK_SPRING_GREEN)


def draw_tree(x, y):
    arcade.draw_triangle_filled(
        x + 40, y,
        x, y - 100,
        x + 80, y - 100,
        arcade.color.DARK_GREEN)
    arcade.draw_lrtb_rectangle_filled(
        x + 30, x + 50,
        y - 100, y - 140,
        arcade.color.DARK_BROWN
    )


arcade.open_window(screen_width, screen_height, "Drawing with Functions")

arcade.start_render()

draw_background()
draw_tree(75, 250)
draw_tree(275, 310)
draw_tree(625, 210)
draw_tree(590, 180)

arcade.finish_render()
arcade.run()
