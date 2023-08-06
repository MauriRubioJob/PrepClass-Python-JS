import arcade

arcade.open_window(800, 600, "MY FIRST WINDOW")
arcade.set_background_color(arcade.color.PUCE_RED)


arcade.start_render()

arcade.draw_point(400, 300, arcade.color.WHITE, 20)

arcade.draw_line(150, 150, 250, 500, arcade.color.ORANGE, 40)

arcade.draw_rectangle_filled(650, 450, 250, 250, arcade.color.YELLOW)

arcade.finish_render()


arcade.run()
