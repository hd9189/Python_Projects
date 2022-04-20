#-------------------------------------------------
#ICS3U
#Hugh Ding
#Final Project
#-------------------------------------------------

#-------------------------------------------------
#Importing neccessary modules
#-------------------------------------------------
from ctypes.wintypes import SIZE
import pygame
import os
import math
import random

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
asteroids = []

#changes the size of the image
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#-------------------------------------------------
#setting constant values to attributes to the classes
#-------------------------------------------------
WHITE = (255, 255, 255)
POINTS = 0
PLAYER1_CONTROLS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_m]
PLAYER2_CONTROLS = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_v]

#-------------------------------------------------
#class for the player
#-------------------------------------------------
class player():
  #set the variables and attributes for the user
  def __init__ (self, pos, player_img, colour, points, controls):
    '''
    Creates attributes for the player class

    args:
      player_img: image
      colour: string
      points: int
      keys_pressed: list
      controls: list
    '''
    self.image = player_img
    self.colour = colour
    self.points = points
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.x_pos = pos[0]
    self.y_pos = pos[1]
    #0: left, 1: right, 2: up, 3: down
    self.controls = controls
    self.angle = 0
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    self.rotated_rect = self.rotate_surf.get_rect()
    self.rotated_rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    #get coordinates of the head of the image
    self.head = (self.x_pos + self.cosine + self.width//2, self.y_pos - self.sine*self.height//2)
    self.bullets = []
    self.last_fired = 0


  #function to help put the 
  def draw(self, WINDOW):
    '''
    puts the players on the window during the game and every update of screen
    '''
    WINDOW.blit(self.rotate_surf, self.rotated_rect)
    #draws the bullets
    for bullet in self.bullets:
      bullet.move()
      bullet.draw(WINDOW)
      if bullet.check_off_screen():
        self.bullets.pop(self.bullets.index(bullet))

  def turnLeft(self):
    '''
    function to change the angle of which the user is facing when specific key is pressed
    '''
    self.angle += 5
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    self.rotated_rect = self.rotate_surf.get_rect()
    self.rotated_rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    self.head = (self.x_pos + self.cosine * self.width//2, self.y_pos - self.sine*self.height//2)

  def turnRight(self):
    '''
    function to change the angle of which the user is facing when specific key is pressed
    '''
    self.angle -= 5
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    self.rotated_rect = self.rotate_surf.get_rect()
    self.rotated_rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    self.head = (self.x_pos + self.cosine * self.width//2, self.y_pos - self.sine*self.height//2)
    
    
  def moveForward(self):
    self.x_pos += self.cosine*5
    self.y_pos -= self.sine*5
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    self.rotated_rect = self.rotate_surf.get_rect()
    self.rotated_rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    self.head = (self.x_pos + self.cosine * self.width//2, self.y_pos - self.sine*self.height//2)

  def moveBackward(self):
    self.x_pos -= self.cosine*5
    self.y_pos += self.sine*5
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    self.rotated_rect = self.rotate_surf.get_rect()
    self.rotated_rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    self.head = (self.x_pos + self.cosine * self.width//2, self.y_pos - self.sine*self.height//2)

  def actions(self, keys_pressed, WINDOW, time):
    if keys_pressed[self.controls[0]]:
      self.turnLeft()
    if keys_pressed[self.controls[1]]:
      self.turnRight()
    if keys_pressed[self.controls[2]]:
      self.moveForward()    
    if keys_pressed[self.controls[3]]:
      self.moveBackward()
    if keys_pressed[self.controls[4]]:
      #use bruteforce to create a time interval between when bullets can be created
      if time-self.last_fired >=120:
        new_bullet = bullet(self)
        new_bullet.draw(WINDOW)
        self.bullets.append(new_bullet)
        self.last_fired = time

  def update_location(self):
    if self.x_pos > WIDTH: self.x_pos = 1
    #use elif to skip additional checking
    elif self.x_pos < 0: self.x_pos = WIDTH-1
    if self.y_pos > HEIGHT: self.y_pos = 1
    elif self.y_pos < 0: self.y_pos = HEIGHT-1

  def collision():
    pass

  def die_respawn():
    pass


class bullet():
  def __init__(self, player):
    #point of creations/release of bullet
    self.point = player.head
    #x and y of the head coordinate
    self.x, self.y = self.point
    #width and height of bullet
    self.w = 4
    self.h = 4
    #get sine and cosine of the player, to know which direction the player is facing when fired so it can go in the direction
    self.c = player.cosine
    self.s = player.sine
    #setting velocity of the bullets no matter the direction
    self.xvelocity = self.c*10
    self.yvelocity = self.s*10

  def move(self):
    self.x += self.xvelocity
    self.y -= self.yvelocity

  def draw(self, WINDOW):
    pygame.draw.rect(WINDOW, (255,255,255), [self.x, self.y, self.w, self.h])

  def check_off_screen(self):
    if self.x < -1 or self.x > WIDTH or self.y <-1 or self.y > HEIGHT:
      return True


# def timer(text, x, y):
#   img = TIMER_FONT.render(text, True, WHITE)
#   WINDOW.blit(img, (x,y))

class asteroid_obj():
  def __init__(self, rank):
    self.rank = rank
    if self.rank == 1: self.height, self.width = ASTEROID_S_SIZE
    elif self.rank == 2: self.height, self.width = ASTEROID_M_SIZE
    elif self.rank == 3: self.height, self.width = ASTEROID_L_SIZE
    #transform size of asteroid
    self.img = pygame.transform.scale(ASTEROID, (self.height, self.width))
    #mainly two parts of the list, to appear from the top or bottom, or from the sides
    #the .randrange() indicates the random value that could be anything, then the .choice() is where the the side it pops out from
    #-1*self.height is when the asteroid is going to appear on the top, in consideration with the images size
    self.rpoint = random.choice([(random.randrange(0, WIDTH-self.width), random.choice([-1*self.height-5, HEIGHT+5])), (random.choice([-1*self.width-5, WIDTH+5]), random.randrange(0, HEIGHT))])
    #gets seperate x and y coordinates
    self.x_pos, self.y_pos = self.rpoint
    #finds the starting point of the asteroid and determindes the direction which the asteroid will go, up or down & left or right
    if self.x_pos < WIDTH//2: self.x_dir = 1
    else: self.x_dir = -1
    if self.y_pos < HEIGHT//2: self.y_dir = 1
    else: self.y_dir = -1
    #velocity of asteroid in x and y
    self.x_vel = self.x_dir*random.randrange(1,3)
    self.y_vel = self.y_dir*random.randrange(1,3)

  def movement(self):
    self.x_pos += self.x_vel
    self.y_pos += self.y_vel

  def draw(self, WINDOW):
    WINDOW.blit(self.img, (self.x_pos, self.y_pos))
  
  def check_off_screen(self):
    if self.x_pos < -70 or self.x_pos > WIDTH+4 or self.y_pos <-70 or self.y_pos > HEIGHT+4:
      return True

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
    if a.check_off_screen():
      asteroids.remove(a)
  



def main():

#-------------------------------------------------
#creating player
#-------------------------------------------------
  player1 = player((WIDTH//4*3, HEIGHT//2), RED_SPACESHIP, WHITE, 0, PLAYER1_CONTROLS)
  player2 = player((WIDTH//4, HEIGHT//2), YELLOW_SPACESHIP, WHITE, 0, PLAYER2_CONTROLS)

  run = True
  clock = pygame.time.Clock()
  time = 0 
  while run:
    if time == 1000: #3 minutes
      break
    #makes the game run at the FPS rate
    clock.tick(FPS)
    time +=1
    if time %20 == 0:
      ran = random.choice([1,1,1,2,2,3])
      asteroids.append(asteroid_obj(ran))

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
    player1.draw(WINDOW)
    player2.draw(WINDOW)
    player1.update_location()
    player2.update_location()

    #update the display every loop
    pygame.display.update()
  #quits and stops the entire game
  pygame.quit()

#runs the main function only if this main file is being run
if __name__ == '__main__':
  main()