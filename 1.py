import pygame
import sys
import math
from datetime import datetime

# Initialize pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")

# Load Mickey's hands images
mickey_hand_seconds = pygame.image.load("mickeyclock.jpeg")
mickey_hand_minutes = pygame.image.load("mickeyclock.jpeg")

# Set the center of the clock
clock_center = (screen_width // 2, screen_height // 2)

def draw_clock():
    # Clear the screen
    screen.fill((255, 255, 255))

    # Get the current time
    now = datetime.now()
    seconds_angle = -now.second * 6  # 6 degrees per second
    minutes_angle = -now.minute * 6  # 6 degrees per minute

    # Rotate Mickey's hands
    rotated_seconds_hand = pygame.transform.rotate(mickey_hand_seconds, seconds_angle)
    rotated_minutes_hand = pygame.transform.rotate(mickey_hand_minutes, minutes_angle)

    # Set the position of the hands
    seconds_hand_pos = (clock_center[0] - rotated_seconds_hand.get_width() // 2,
                        clock_center[1] - rotated_seconds_hand.get_height() // 2)
    minutes_hand_pos = (clock_center[0] - rotated_minutes_hand.get_width() // 2,
                        clock_center[1] - rotated_minutes_hand.get_height() // 2)

    # Draw Mickey's hands
    screen.blit(rotated_seconds_hand, seconds_hand_pos)
    screen.blit(rotated_minutes_hand, minutes_hand_pos)

    # Update the display
    pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_clock()
    pygame.time.delay(1000)  # Update every second
