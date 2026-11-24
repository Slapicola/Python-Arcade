# Run Command: py -3.12 test.py

"""
Minimal Sprite Example

Draws a single sprite in the middle screen.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_minimal
"""
import arcade


class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        

    def on_draw(self):
        # 3. Clear the screen
        self.clear()

        # 4. Draw a Rectangle
        arcade.draw_lrbt_rectangle_filled(100, 1200, 20, 700, arcade.color.WHITE)

        # Darw a line
        arcade.draw_line(200, 50, 200, 600, arcade.color.BLACK, 10)

        # 5. Draw an outlined circle (practice for Xs and Os)
        arcade.draw_circle_outline(400, 300, 50, arcade.color.GREEN)



def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(1280, 720, "Drawing test Example")

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()