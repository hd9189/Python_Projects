import pygame
import os

#constant values should be all caps
WIDTH, HEIGHT = 900, 500
#creat window of the size of width height
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#title for window
pygame.display.set_caption("Space_Game")

WHITE = (255,255,255)
BLACK = (0,0,0)

BORDER = pygame.Rect((WIDTH/2) - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 3 #speed of movement
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45

#load image to game
#using os to find the path, and using .join to join the path together to get image
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

#resizing the image by height and width and rotating the image at the same time by degrees, both part of transform function
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)

BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets', 'space.png'))

def draw_window(red, yellow):
    #fill the window with certain colour, use RGB number
    #fill screen first, because it will overlap the objects
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    #use blit to draw a surface onto the screen, the objects are a surface, its part of the window function
    #defining the positions of the ships. in pygame the top left corner is (0,0), the image is drawn from the top left corner of the image
    #parameters are defined throught the parameters for the rectangle, and since its linked to rectangle, it will move with the rectangle
    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x, red.y))

    #have to update the screen manually
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    #K_ are the keys from pygame module
    if keys_pressed[pygame.K_a]: #LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]: #RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_s]: #DOWN
        yellow.y += VEL
    if keys_pressed[pygame.K_w]: #UP, the y axis is positive as you go down
        yellow.y -= VEL

def red_handle_movement(keys_pressed, red):
    #K_ are the keys from pygame module
    if keys_pressed[pygame.K_LEFT]: #LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT]: #RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_DOWN]: #DOWN
        red.y += VEL
    if keys_pressed[pygame.K_UP]: #UP, the y axis is positive as you go down
        red.y -= VEL

#handle the logic in the game
def main():
    #create 2 rectangles to represent the spaceship to help the move around
    #(x position, y position, width of shape, height of shape)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    #pygame function to make a clock object
    clock = pygame.time.Clock()
    run = True

    #to stop the window from instantly closing
    while run:
        #controlling the speed of the while loop, to have the cap of FPS value
        clock.tick(FPS)

        #get a list of all the events inside the game
        for event in pygame.event.get():
            #if the user quits close window, quits once the x button is pressed
            if event.type == pygame.QUIT:
                run = False
        
        #the key movement method allows multiple key inputs at the same time
        #this get_pressed from key tells us what keys are being pressed down, so look at all keys, and register it
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        

        #red and yellow parameters
        draw_window(red,yellow)
        
    
    pygame.quit()

#only run this function if your starting it from this file
if __name__ == "__main__":
    main()