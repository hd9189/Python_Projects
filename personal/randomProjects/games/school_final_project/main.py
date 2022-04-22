#-------------------------------------------------
#ICS3U
#Hugh Ding
#Final Project
#-------------------------------------------------

#-------------------------------------------------
#Importing neccessary modules
#-------------------------------------------------
import pygame
import os
import math
import random
from classes import player
from classes import bullet
from classes import asteroid_obj
#-------------------------------------------------
#defining constant values that won't be changed
#-------------------------------------------------

#defining fonts
#TIMER_FONT = pygame.font.SysFont("comicsans", 40)

#defining the fps
FPS = 60

#defining the width and height of the window
WIDTH, HEIGHT = 1000, 750

#constant values of spaceship size
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45
#-------------------------------------------------
#setting the screen
#-------------------------------------------------
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
#setting the window title
pygame.display.set_caption("Asteroid Smash!")


#-------------------------------------------------
#loading images from folder
#-------------------------------------------------
#defining the images, find the path to the image and loads it and transforms the image to fit the size of the window
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Images', 'background.jpg')), (WIDTH, HEIGHT))
RED_SPACESHIP = pygame.image.load(
    os.path.join('Images', 'spaceship_red.png'))
YELLOW_SPACESHIP = pygame.image.load(
    os.path.join('Images', 'spaceship_yellow.png'))

ASTEROID = pygame.image.load(
    os.path.join('Images', 'asteroid.png'))
ASTEROID_S_SIZE = (25,25)
ASTEROID_M_SIZE = (50,50)
ASTEROID_L_SIZE = (75,75)
asteroids = pygame.sprite.Group()

#changes the size of the image
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#-------------------------------------------------
#setting constant values to attributes to the classes
#-------------------------------------------------
WHITE = (255, 255, 255)
RED = (255,0,0)
YELLOW = (255,255,0)
POINTS = 0
PLAYER1_CONTROLS = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_v]
PLAYER2_CONTROLS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_m]

def draw_window(time):
  '''
  main function to draw the window, so everything that is to be put on the window will be in this function
  '''
  #puts the background as the image
  # timer(time, WIDTH/4, HEIGHT-10)
  WINDOW.blit(BACKGROUND, (0, 0))
  for a in asteroids:
    a.movement()
    a.draw(WINDOW)
    if a.check_off_screen(WIDTH, HEIGHT):
      asteroids.remove(a)

def main():

#-------------------------------------------------
#creating player
#-------------------------------------------------
  player1 = player((WIDTH//4, HEIGHT//2), RED_SPACESHIP, RED, 0, PLAYER1_CONTROLS)
  player2 = player((WIDTH//4*3, HEIGHT//2), YELLOW_SPACESHIP, YELLOW, 0, PLAYER2_CONTROLS)

  run = True
  clock = pygame.time.Clock()
  time = 0 
  while run:
    if time == 1000: #3 minutes
      break
    #makes the game run at the FPS rate
    clock.tick(FPS)
    time +=1
    if time %30 == 0:
      ran = random.choice([1,1,1,2,2,3])
      asteroids.add(asteroid_obj(ran, WIDTH, HEIGHT, ASTEROID))

    #this get_pressed from key tells us what keys are being pressed down, so look at all keys, and register it
    keys_pressed = pygame.key.get_pressed()
    player1.actions(keys_pressed, WINDOW, time)
    player2.actions(keys_pressed, WINDOW, time)

    #sets interval limit
    pygame.key.set_repeat(0,1)

    #loops through all the events that happen in the game
    for event in pygame.event.get():
      #if the even that the for loop received type is the same as the quit event
      if event.type == pygame.QUIT:
        #stops while loop
        run = False

    #draws the window again every time
    time = pygame.time.get_ticks()

    draw_window(time)
    player1.draw(WINDOW, WIDTH, HEIGHT)
    player2.draw(WINDOW, WIDTH, HEIGHT)
    player1.update_location(WIDTH, HEIGHT)
    player2.update_location(WIDTH, HEIGHT)

    #update the display every loop
    pygame.display.update()
  #quits and stops the entire game
  pygame.quit()

#runs the main function only if this main file is being run
if __name__ == '__main__':
  main()