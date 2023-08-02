import pygame


class Settings:
    """A class to store all settings for Rotating Right Triangle."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Set the dimensions of the window
        self.width, self.height = 800, 800

        # Create the window
        self.window = pygame.display.set_mode((self.width, self.height))

        # Set the color of the lines
        self.object_colors = {
            'black': (0, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'red': (255, 0, 0),
            'white': (255, 255, 255)
        }

        # Get the center coordinates of the window
        self.center_x, self.center_y = self.width // 2, self.height // 2

        # Initialize the angle for the line
        self.angle = 0

        # Define the speed of the line movement
        self.line_speed = 1

        # Calculate the initial coordinates of the edge of the circle
        self.edge_x = self.center_x
        self.edge_y = self.center_y - 400

        # Initialize the direction of the line movement
        self.line_direction = 0

        # Create a font for the text
        self.font = pygame.font.SysFont(None, 24)