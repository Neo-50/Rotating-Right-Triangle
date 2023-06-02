import pygame
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width, height = 800, 800

# Create the window
window = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Circle and Line Drawing")

# Set the color of the circle and line (RGB format)
circle_color = (0, 0, 0)      # Black
line1_color = (255, 0, 0)     # Red
line2_color = (0, 255, 0)     # Green
line3_color = (0, 0, 255)     # Blue
angle_txt_color = (0, 0, 0)   # Black
line2_txt_color = (0, 255, 0) # Green
line3_txt_color = (0, 0, 255) # Blue

# Get the center coordinates of the window
center_x, center_y = width // 2, height // 2

# Initialize the angle for the line
angle = 0

# Define the speed of the line movement
line_speed = .02

# Calculate the initial coordinates of the edge of the circle
edge_x = center_x
edge_y = center_y - 400

# Initialize the direction of the line movement
line_direction = 0

# Create a font for the text
font = pygame.font.SysFont(None, 24)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                line_direction = -1  # Move the line clockwise
            elif event.key == pygame.K_LEFT:
                line_direction = 1  # Move the line counterclockwise
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                line_direction = 0  # Stop the line movement

    # Fill the window with white color
    window.fill((255, 255, 255))

    # Calculate the updated angle based on the line direction
    angle += line_speed * line_direction

    # Reset the angle to zero after it passes 360
    if angle > 360:
        angle = 0
    elif angle < -360:
        angle = 0

    # Calculate the updated coordinates of the edge of the circle
    edge_x = center_x + 400 * math.cos(math.radians(angle))  # Update the x coordinate
    edge_y = center_y - 400 * math.sin(math.radians(angle))  # Update the y coordinate

    # Calculate the length of line_2
    line_2_len = abs(edge_x - 400)

    # Calculate the length of line_3
    line_3_len = abs(400 - edge_y)

    # Draw a line from the center to the edge of the circle (line_1)
    pygame.draw.line(window, line1_color, (center_x, center_y), (edge_x, edge_y))

    # Draw line_2 from the center to line_3
    pygame.draw.line(window, line2_color, (400, 400), (edge_x, 400))

    # Draw line_3 from the edge of the circle to the intersection point with line_2
    pygame.draw.line(window, line3_color, (edge_x, edge_y), (edge_x, 400))

    # Draw a circle with the center at (400, 400) or the center of the window
    pygame.draw.circle(window, circle_color, (center_x, center_y), 400, 1)  # Radius = 400, Width = 1

    # Create the text surface for angle
    angle_text = font.render("angle: " + str(round(angle, 2)), True, angle_txt_color)

    # Create the text surface for line_2 length
    line2_text = font.render("line_2 len: " + str(round(line_2_len, 2)), True, line2_txt_color)

    # Create the text surface for line_3 length
    line3_text = font.render("line_3 len: " + str(round(line_3_len, 2)), True, line3_txt_color)

    # Create the text surface for x and y coordinates
    xy_text = font.render(f"xval: {str(round(edge_x, 2))} yval: {str(round(edge_y, 2))}", True, angle_txt_color)

    # Create the text surface for cos
    cos_text = font.render(f"cosine: {round(math.cos(math.radians(angle)), 2)}", True, angle_txt_color)

    # Create the text surface for sin
    sin_text = font.render(f"sine: {round(math.sin(math.radians(angle)), 2)}", True, angle_txt_color)

    # Get the rect object for angle text
    angle_rect = angle_text.get_rect()

    # Get the rect object for line_2 text
    line2_rect = line2_text.get_rect()

    # Get the rect object for line_3 text
    line3_rect = line3_text.get_rect()

    # Get the rect object for xy_text
    xy_rect = line3_text.get_rect()

    # Get the rect object for cos_text
    cos_rect = cos_text.get_rect()

    # Get the rect object for sin_text
    sin_rect = sin_text.get_rect()

    # Set the position of angle text in the upper right corner
    angle_rect.topright = (width - 30, 10)

    # Set the position of line_2 len text below the angle text
    line2_rect.topright = (width - 30, angle_rect.bottom + 10)

    # Set the position of line_3 len text below the line_2 text
    line3_rect.topright = (width - 30, line2_rect.bottom + 10)

    # Set the position of xy_text below the line_3 text
    xy_rect.topright = (width - 80, line3_rect.bottom + 10)

    # Set the position of cos_text
    cos_rect.center = (width // 2, 650)

    # Set the position of sin_text
    sin_rect.center = (width // 2, cos_rect.bottom + 10)

    # Draw the angle text and line_3 text on the window surface
    window.blit(angle_text, angle_rect)
    window.blit(line2_text, line2_rect)
    window.blit(line3_text, line3_rect)
    window.blit(xy_text, xy_rect)
    window.blit(cos_text, cos_rect)
    window.blit(sin_text, sin_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
