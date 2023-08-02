import math
import pygame


def update_angle(angle, speed, direction):
    # Calculate the updated angle based on the line direction
    angle += speed * direction
    return angle


def reset_angle(angle):
    # Reset angle after it passes 360
    if angle > 360:
        angle = 0
    elif angle < -360:
        angle = 0
    return angle


def update_coords(centerx, centery, angle):
    # Calculate the updated coordinates of the edge of the circle
    edgex = centerx + 400 * math.cos(math.radians(angle))  # Update the x coordinate
    edgey = centery - 400 * math.sin(math.radians(angle))  # Update the y coordinate
    return edgex, edgey


def line_lengths(edgex, edgey):
    # Calculate the length of line_2
    line_2_len = abs(edgex - 400)

    # Calculate the length of line_3
    line_3_len = abs(400 - edgey)

    return line_2_len, line_3_len


def draw_objects(window, colors, centerx, centery, edgex, edgey):
    # Draw a line from the center to the edge of the circle (line_1)
    pygame.draw.line(window, colors['red'], (centerx, centery),
                     (edgex, edgey))

    # Draw line_2 from the center to line_3
    pygame.draw.line(window, colors['green'], (400, 400), (edgex, 400))

    # Draw line_3 from the edge of the circle to the intersection point with line_2
    pygame.draw.line(window, colors['blue'], (edgex, edgey),
                     (edgex, 400))

    # Draw a circle with the center at (400, 400) or the center of the window
    pygame.draw.circle(window, colors['white'], (centerx, centery), 400, 1)


def draw_text(angle, line2len, line3len, edgexval, edgeyval, width,
              window, font, colors):

    texts = [
        ("angle: ", angle, colors['white']),
        ("line_2 len: ", line2len, colors['green']),
        ("line_3 len: ", line3len, colors['blue']),
        ("xval: ", edgexval, colors['white']),
        ("yval: ", edgeyval, colors['white']),
    ]

    sincos = [
        ("cos: ", angle, colors['white']),
        ("sin: ", angle, colors['white']),
    ]

    for i, (text, num, color) in enumerate(texts):
        text_surface = font.render(text + str(round(num, 2)), True, color)
        text_rect = text_surface.get_rect()
        text_rect.topright = (770, 10 + i * 30)
        window.blit(text_surface, text_rect)

    for i, (text, angle, color) in enumerate(sincos):
        if i == 0:
            val = str(round(math.cos(math.radians(angle)), 2))
        else:
            val = str(round(math.sin(math.radians(angle)), 2))
        text_surface = font.render(text + val, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (width // 2, 600 + i * 30)
        window.blit(text_surface, text_rect)
