# Run Command: py -3.12 test.py

import arcade

# Set Rows and Columns
ROW_COUNT = 3
COLUMN_COUNT = 3

# Set the Width and Height of each grid location
WIDTH = 150
HEIGHT = 150

# Set margins
MARGINS = 5

# Math to figure out screen dimensions
WINDOW_WIDTH = (WIDTH + MARGINS) * COLUMN_COUNT + MARGINS
WINDOW_HEIGHT = (HEIGHT + MARGINS) * ROW_COUNT + MARGINS

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # Create a two-dimensional array
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)
        

    def on_draw(self):
        # 3. Clear the screen
        self.clear()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = (MARGINS + WIDTH) * column + MARGINS + WIDTH // 2
                y = (MARGINS + HEIGHT) * row + MARGINS + HEIGHT // 2

                # Draw the box
                arcade.draw_rect_filled(arcade.rect.XYWH(x, y, WIDTH, HEIGHT), arcade.color.WHITE)

        # # 5. Draw an outlined circle (practice for Xs and Os)
        # arcade.draw_circle_outline(400, 300, 50, arcade.color.GREEN)



def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Tic-Tac-Toe")

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()