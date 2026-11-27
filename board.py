# Run Command: py -3.12 board.py

import arcade

# Set Rows and Columns
ROW_COUNT = 3
COLUMN_COUNT = 3

# Set the Width and Height of each grid location
WIDTH = 150
HEIGHT = 150

# Set margins
MARGINS = 5

# Math to figure out board dimensions
BOARD_WIDTH = (WIDTH + MARGINS) * COLUMN_COUNT + MARGINS
BOARD_HEIGHT = (HEIGHT + MARGINS) * ROW_COUNT + MARGINS

# Set height and width for the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # Create a two-dimensional array
        # looks like this:
        # [
        #       [0, 0, 0],
        #       [0, 0, 0],
        #       [0, 0, 0]
        # ]
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

    # testing for on_mouse_press() (Checks where the mouse is clicked)
    # (prints the coordinates to the console.)
    def on_mouse_press(self, x, y, button, modifiers):
        if (x >= 170 and x <= 316 and y >= 347 and y <= 489):
            print("Clicked at: Top Left")
        elif (x >= 326 and x <= 472 and y >= 346 and y <= 487):
            print("Clicked at: Top Middle")
        elif (x >= 476 and x <= 622 and y >= 346 and y <= 487):
            print("Clicked at: Top Right")
        elif (x >= 170 and x <= 316 and y >= 197 and y <= 339):
            print("Clicked at: Middle Left")
        elif (x >= 326 and x <= 472 and y >= 196 and y <= 337):
            print("Clicked at: Middle Middle")
        elif (x >= 476 and x <= 622 and y >= 196 and y <= 337):
            print("Clicked at: Middle Right")
        elif (x >= 170 and x <= 316 and y >= 39 and y <= 189):
            print("Clicked at: Bottom Left")
        elif (x >= 326 and x <= 472 and y >= 39 and y <= 189):
            print("Clicked at: Bottom Middle")
        elif (x >= 476 and x <= 622 and y >= 39 and y <= 189):
            print("Clicked at: Bottom Right")

        print(f"Clicked at: x = {x}, y = {y}")
            
        

    def on_draw(self):
        # Clear the screen
        self.clear()

        # Draw title
        arcade.draw_text("Tic-Tac-Toe", 300, 500, arcade.color.WHITE, 40)

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = (MARGINS + WIDTH) * column + MARGINS + WIDTH // 2
                y = (MARGINS + HEIGHT) * row + MARGINS + HEIGHT // 2

                # Draw the box
                arcade.draw_rect_filled(arcade.rect.XYWH(x + 165, y + 25, WIDTH, HEIGHT), arcade.color.WHITE)

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