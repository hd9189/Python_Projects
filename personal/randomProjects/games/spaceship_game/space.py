import pygame
import os
#initialize font
pygame.font.init()
#initialize sounds in pygame
pygame.mixer.init()

#constant values should be all caps
WIDTH, HEIGHT = 900, 500
#creat window of the size of width height
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#title for window
pygame.display.set_caption("Space_Game")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect((WIDTH//2) - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Assets_Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Assets_Gun+Silencer.mp3'))

FPS = 60
VEL = 5 #speed of movement
BULLET_VEL = 12
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WIN_FONT = pygame.font.SysFont("comicsans", 100)

#custom event for collision, use different number to give different number
YELLOW_HIT = pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT +2

#load image to game
#using os to find the path, and using .join to join the path together to get image
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

#resizing the image by height and width and rotating the image at the same time by degrees, both part of transform function
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    #fill the window with certain colour, use RGB number
    #fill screen first, because it will overlap the objects
    #have to fill every time, because pygame will not remove the last version of the picture
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    #putting words onto the screen
    #using render to render text
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)

    #putting words onto the window
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width()-10, 10))
    WIN.blit(yellow_health_text, (10, 10))


    #use blit to draw a surface onto the screen, the objects are a surface, its part of the window function
    #defining the positions of the ships. in pygame the top left corner is (0,0), the image is drawn from the top left corner of the image
    #parameters are defined throught the parameters for the rectangle, and since its linked to rectangle, it will move with the rectangle
    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    #have to update the screen manually
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    #K_ are the keys from pygame module
    #seeing if you continue to press the keys will you go off screen
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x : #RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT-15: #DOWN
        yellow.y += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #UP, the y axis is positive as you go down
        yellow.y -= VEL

def red_handle_movement(keys_pressed, red):
    #K_ are the keys from pygame module
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT-15 : #DOWN
        red.y += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #UP, the y axis is positive as you go down
        red.y -= VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    #looping through all the bullets fired
    for bullet in yellow_bullets:
        #moving the bullet in fired direction
        bullet.x += BULLET_VEL
        #func in pygame called colliderect, which check if a object collired with another object, only can be used if both are rectangles
        if red.colliderect(bullet):
            #create new event so that the main function can check and do something when this event happens
            pygame.event.post(pygame.event.Event(RED_HIT))
            #make bullet dissapear
            yellow_bullets.remove(bullet)
        #remove bullet when it gets off the screen
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WIN_FONT.render(text,1,WHITE)
    #get width of text
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2 ))
    #update the display
    pygame.display.update()
    #delay the game from restarting for 5 secs
    pygame.time.delay(5000)

#handle the logic in the game
def main():
    #create 2 rectangles to represent the spaceship to help the move around
    #(x position, y position, width of shape, height of shape)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    #list of bullets on screen
    red_bullets = []
    yellow_bullets = []

    #health of players
    red_health = 5
    yellow_health = 5

    winner_text = ""

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
                pygame.quit()
            
            #check if the key is down
            if event.type == pygame.KEYDOWN:
                #checks which key is down, and you can't just hold the key down to spam bullets
                if event.key == pygame.K_g and len(yellow_bullets) < MAX_BULLETS:
                    #use flat division because it cant be a float
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10,5)
                    yellow_bullets.append(bullet)
                    #play sound
                    BULLET_FIRE_SOUND.play()
                
                if event.key == pygame.K_m and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10,5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
        
            if event.type == RED_HIT:
                red_health -=1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        if red_health == 0:
            winner_text = "YELLOW wins!"

        if yellow_health == 0:
            winner_text = "RED wins!"
        
        #means theres a winner to initialize the draw winner func
        if winner_text != "":
            draw_winner(winner_text)
            break

        #the key movement method allows multiple key inputs at the same time
        #this get_pressed from key tells us what keys are being pressed down, so look at all keys, and register it
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        #red and yellow parameters
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        
    
    main()

#only run this function if your starting it from this file
if __name__ == "__main__":
    main()