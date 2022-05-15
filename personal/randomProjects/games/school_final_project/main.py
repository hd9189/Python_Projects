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
import random
from classes import player
from classes import bullet_group
from classes import asteroid_obj
#-------------------------------------------------
#defining constant values that won't be changed
#-------------------------------------------------

#initialize font
pygame.font.init()
#initialize sounds in pygame
pygame.mixer.init()

#defining the fpsm
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
    os.path.join('Assets', 'background.jpg')), (WIDTH, HEIGHT))
RED_SPACESHIP = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
YELLOW_SPACESHIP = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))

ASTEROID = pygame.image.load(
    os.path.join('Assets', 'asteroid.png'))
ASTEROID_S_SIZE = (25,25)
ASTEROID_M_SIZE = (50,50)
ASTEROID_L_SIZE = (75,75)
asteroids = pygame.sprite.Group()

#changes the size of the image
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#sound
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Bullet_hit.mp3'))
BULLET_HIT_SOUND.set_volume(0.1)
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Bullet_fire.mp3'))
BULLET_FIRE_SOUND.set_volume(0.05)
PLAYER_DIE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Die_sound.mp3'))
PLAYER_DIE_SOUND.set_volume(0.3)
ASTEROID_HIT_PLAYER_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Player_hit_sound.mp3'))
ASTEROID_HIT_PLAYER_SOUND.set_volume(0.2)
PLAYER_HIT_PLAYER_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Player_hit_player_sound.mp3'))
PLAYER_HIT_PLAYER_SOUND.set_volume(0.3)

#fonts
HEALTH_FONT = pygame.font.SysFont("comicsans", 20)
WIN_FONT = pygame.font.SysFont("comicsans", 100)

#positions for player
TEXT_POSITION = [(10, 10), (WIDTH - 86 - 10, 10), (10, HEIGHT- 28 -10), (WIDTH - 86-10, HEIGHT - 28-10)] #order is in player 1,2,3,4
#height of text = 28
#width of text = 86
#points text should be under health text

#-------------------------------------------------
#setting constant values to attributes to the classes
#-------------------------------------------------
WHITE = (255, 255, 255)
RED = (255,0,0)
YELLOW = (255,255,0)
POINTS = 0
PLAYER1_CONTROLS = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_v]
PLAYER2_CONTROLS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_m]

#-------------------------------------------------
#creating player
#-------------------------------------------------
player_list = [
  player((WIDTH//4, HEIGHT//2), RED_SPACESHIP, RED, PLAYER1_CONTROLS, BULLET_FIRE_SOUND),
  player((WIDTH//4*3, HEIGHT//2), YELLOW_SPACESHIP, YELLOW, PLAYER2_CONTROLS, BULLET_FIRE_SOUND)
]


def collision_group(player, asteroid):
  '''
  Uses groupcollision to if the bullet sprite group and the asteroids sprite group collide. Adds points depending on the size of the asteroid, and creates new asteroid objects if the asteroid destroyed was not the smallest one.

  parameters:
    player: object
    asteroid: list/sprite group

  return:
    points: int
  '''
  collide = pygame.sprite.groupcollide(player.bullets, asteroid, True, True) #dictionary of collided objects
  #^dokill 1 and 2 asks if you want to delete if the objects collide
  points = 0
  for b in collide.keys():
    bullet_group.remove(b) #remove bullet from the bullets group that contains all bullets
  for a in collide.values():
    BULLET_HIT_SOUND.play()
    a = a[0] #because .groupcollide returns the value as a list
    if a.rank > 1: #creates new smaller asteroids, disbursing from the asteroid
      if a.rank == 3: points += 3
      elif a.rank == 2: points += 2
      a.destroy_respawn(a, WIDTH, HEIGHT, ASTEROID, asteroids)
      # ran = random.randrange(2,4)
      # for x in range(ran):
      #   new_asteroid = asteroid_obj(a.rank-1, WIDTH, HEIGHT, ASTEROID)
      #   new_asteroid.x_pos = a.x_pos
      #   new_asteroid.y_pos = a.y_pos
      #   asteroids.add(new_asteroid)
    else: points += 1

  return points

def player_collision_check(player, bullet, asteroid):
  '''
  checks the collision of the player and takes away lives of player every hit, also makes the player immortal after being hit

  Parameters:
    player: player object along with its attributes
    bullet: sprite group with the group of bullet sprites of the other player
    asteroid: the group of asteroid sprites

  Returns:
    points_deducted: int value where it returns 3 points for everytime the player hits the other player
  '''
  collision_a = pygame.sprite.spritecollide(player, asteroid, True)
  collision_b = pygame.sprite.spritecollide(player, bullet, True)
  if not player.immor and len(collision_a) !=0:
    player.lives -= len(collision_a)
    #player.immor = True
    ASTEROID_HIT_PLAYER_SOUND.play()
    a = collision_a[0] #collision is a lsit
    if a.rank > 1:
      a.destroy_respawn(a, WIDTH, HEIGHT, ASTEROID, asteroids)
    return 1 #1 point deducted for every asteriod hit
  elif not player.immor and len(collision_b) !=0:
    PLAYER_HIT_PLAYER_SOUND.play()
    player.lives -= len(collision_b)
    player.immor == True
    for p in player_list:
      if collision_b[0] in p.bullets:
        p.bullets.remove(collision_b[0])
        break

    return 3 #3 deducted for every collision with bullet

  return 0

def draw_window():
  '''
  main function to draw the window, so everything that is to be put on the window will be in this function

  Parameters:
    None
  
  Returns:
    None
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
  '''
  main function that runs the game

  Parameters:m
    None

  Returns:
    None
  '''



  run = True
  clock = pygame.time.Clock()
  time = 0 
  while run:
    if time > 180000: #3 minutesv
      run = False
    #makes the game run at the FPS rate
    clock.tick(FPS)
    time +=1
    if time %30 == 0:
      ran = random.choice([1,1,1,2,2,3])
      asteroids.add(asteroid_obj(ran, WIDTH, HEIGHT, ASTEROID))

    #this get_pressed from key tells us what keys are being pressed down, so look at all keys, and register it
    keys_pressed = pygame.key.get_pressed()
    for user in range(len(player_list)):
      player_list[user].actions(keys_pressed, WINDOW, time)
      player_list[user].points += collision_group(player_list[user], asteroids)
      player_list[user].points -= player_collision_check(player_list[user], bullet_group, asteroids)
      # player1.actions(keys_pressed, WINDOW, time)
      # player2.actions(keys_pressed, WINDOW, time)
      # player1.points += collision_group(player1, asteroids)
      # player2.points += collision_group(player2, asteroids)
      # player2.points += player_collision_check(player1, player2.bullets, asteroids)
      # player1.points += player_collision_check(player2, player1.bullets, asteroids)
      # print("player 1:", player1.points)
      # print("player 2:", player2.points)


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

    draw_window()
    for p in range(len(player_list)):
      player_list[p].draw(WINDOW, WIDTH, HEIGHT)
      player_list[p].update_location(WIDTH, HEIGHT)
      # player1.draw(WINDOW, WIDTH, HEIGHT)
      # player1.update_location(WIDTH, HEIGHT)
      # player2.draw(WINDOW, WIDTH, HEIGHT)
      # player2.update_location(WIDTH, HEIGHT)
      player_health = HEALTH_FONT.render("Health: " + str(player_list[p].lives), 1, WHITE)
      player_points = HEALTH_FONT.render("Points: " + str(player_list[p].points),1, WHITE)
      WINDOW.blit(player_health, TEXT_POSITION[p])
      WINDOW.blit(player_points, (TEXT_POSITION[p][0], TEXT_POSITION[p][1]+30))

    #update the display every loop
    pygame.display.update()
    # print(time)
  #quits and stops the entire game
  pygame.quit()

#runs the main function only if this main file is being run
if __name__ == '__main__':
  main()

  #PROBLEMS:
  #bullets are colliding with the player itself, create copy of bullet group and remove all the players own bullets