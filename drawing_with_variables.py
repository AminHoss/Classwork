import arcade

WIDTH = 640
HEIGHT = 480
x = WIDTH/2
y = HEIGHT/2
radius = 60

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

arcade.draw_circle_filled(x, y, radius, arcade.color.BLUE_GREEN)

arcade.finish_render()
arcade.run()