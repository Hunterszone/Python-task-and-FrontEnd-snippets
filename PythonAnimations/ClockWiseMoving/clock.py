# Import a library of functions called 'pygame'
import pygame
import math
 
# Initialize the game engine
pygame.init()
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
PI = 3.141592653
 
# Set the height and width of the screen
size = [400, 400]
screen = pygame.display.set_mode(size)
 
my_clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
 
angle = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Set the screen background
    screen.fill(WHITE)
 
    # Dimensions of radar sweep
    # Start with the top left at 20,20
    # Width/height of 250
    box_dimensions = [20, 20, 220, 220]
 
    # Draw the outline of a circle to 'sweep' the line around
    pygame.draw.ellipse(screen, BLACK, box_dimensions, 2)
 
    # Draw a black box around the circle
    pygame.draw.rect(screen, BLACK, box_dimensions, 2)
 
    # Calculate the x,y for the end point of our 'sweep' based on
    # the current angle
    x = 125 * math.sin(angle) + 145
    y = 125 * math.cos(angle) + 145
 
    # Draw the line from the center at 145, 145 to the calculated
    # end spot
    pygame.draw.line(screen, RED, [130, 130], [x-20, y-50], 2)
 
    # Increase the angle by 0.03 radians
    #if + .03 => counter clockwise rotation
    #if - .03 => clockwise rotation
    angle = angle - .03

    #draw a circle around the center
    pygame.draw.circle(screen, BLACK, (130, 130), 20, 2)

    #draw a clock
    clockImg = pygame.image.load('clock.png')
    clockx = 7
    clocky = 7
    
    screen.blit(clockImg, (clockx, clocky))
    
 
    # If we have done a full sweep, reset the angle to 0
    if angle > 2 * PI:
        angle = angle - 2 * PI
 
    # Flip the display, wait out the clock tick
    pygame.display.flip()
    my_clock.tick(60)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
