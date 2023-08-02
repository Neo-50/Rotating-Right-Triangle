import pygame
import math
from settings import Settings
import functions as gf


def run_game():
    # Initialize pygame and settings
    pygame.init()
    cset = Settings()

    # Set the title of the window
    pygame.display.set_caption("Circle and Line Drawing")

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    cset.line_direction = -1  # Move the line clockwise
                elif event.key == pygame.K_LEFT:
                    cset.line_direction = 1  # Move the line counterclockwise
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    cset.line_direction = 0  # Stop the line movement

        # Fill the window with black color
        cset.window.fill((0, 0, 0))

        # Update the angle for the right triangle
        cset.angle = gf.update_angle(cset.angle, cset.line_speed, cset.line_direction)

        # Reset angle to zero after it passes 360
        cset.angle = gf.reset_angle(cset.angle)

        # Calculate coordinates for a point the edge of the circle based on angle
        edgexval, edgeyval = gf.update_coords(cset.edge_x, cset.edge_y, cset.center_x, cset.center_y, cset.angle)

        # Calculate the line lengths
        line2len, line3len = gf.line_lengths(edgexval, edgeyval)

        # Draw the circle and lines
        gf.draw_objects(cset.window, cset.object_colors, cset.center_x,
                        cset.center_y, edgexval, edgeyval)
        # Draw the text
        gf.draw_text(cset.angle, line2len, line3len, edgexval, edgeyval,
                     cset.width, cset.window, cset.font, cset.object_colors)

        # Update the display
        pygame.display.flip()

        # Set the framerate
        pygame.time.Clock().tick(10)


run_game()
