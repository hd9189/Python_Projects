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
from classes import player, asteroid_obj, explosion, bullet_group, explosions_q, power_up
from screens import WIDTH, HEIGHT, FPS, home, how_to_play, win, how_to_play_next
#-------------------------------------------------
#defining constant values that won't be changed
#-------------------------------------------------

#initialize all pygame modules
pygame.init()


#constant values of spaceship size
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 45
#-------------------------------------------------
#setting the screen
#-------------------------------------------------

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
#setting the window title
pygame.display.set_caption("Cosmic Cavaliers")

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
TIME_FONT = pygame.font.SysFont("arial", 30)

#positions for player
TEXT_POSITION = [(10, 10), (WIDTH - 86 - 15, 10)] #order is in player 1,2,3,4
#height of text = 28
#width of text = 86
#points text should be under health text

#sprite group of power ups
power_up_group = pygame.sprite.Group()

#-------------------------------------------------
#setting constant values to attributes to the classes
#-------------------------------------------------
#RGB values
WHITE = (255, 255, 255)
RED = (255,0,0)
YELLOW = (255,255,0)
POINTS = 0
PLAYER1_CONTROLS = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_v]
PLAYER2_CONTROLS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_m]

#-------------------------------------------------
#creating player
#-------------------------------------------------
player_pos = [(WIDTH//4, HEIGHT//2), (WIDTH//4*3, HEIGHT//2)]
player_list = [
  player(player_pos[0], RED_SPACESHIP, RED, PLAYER1_CONTROLS, BULLET_FIRE_SOUND),
  player(player_pos[1], YELLOW_SPACESHIP, YELLOW, PLAYER2_CONTROLS, BULLET_FIRE_SOUND)
]


def collision_group(player, asteroid, time):
  '''
  Uses groupcollision to if the bullet sprite group and the asteroids sprite group collide. Adds points depending on the size of the asteroid, and creates new asteroid objects if the asteroid destroyed was not the smallest one.

  parameters:
    player: object
    asteroid: list/sprite group
    time: int

  return:
    points: int
  '''

  collide = pygame.sprite.groupcollide(player.bullets, asteroid, True, True) #dictionary of collided objects
  #^dokill 1 and 2 asks if you want to delete if the objects collide

  points = 0
  #for loop that loops through the keys of returned group collide value
  for b in collide.keys():
    #every bullet in collide
    bullet_group.remove(b) #remove bullet from the bullets group that contains all bullets
  #every asteroid in collide
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
    else: 
      #if asteroid is the smallest one, create explosion object 
      asteroid_explosion = explosion(a.x_pos, a.y_pos)
      asteroid_explosion.enter_q(time)
      points += 1
        

  return points

def player_collision_check(player, bullet, asteroid, power_ups, time):
  '''
  checks the collision of the player and takes away lives of player every hit, also makes the player immortal after being hit

  Parameters:
    player: player object along with its attributes
    bullet: sprite group with the group of bullet sprites of the other player
    asteroid: the group of asteroid sprites
    power_ups: power_up group sprite
    time: int

  Returns:
    points_deducted: int value where it returns 3 points for everytime the player hits the other player
  '''
  #track collision of each sprite group
  collision_a = pygame.sprite.spritecollide(player, asteroid, True)
  collision_b = pygame.sprite.spritecollide(player, bullet, False)
  collision_p = pygame.sprite.spritecollide(player, power_ups, True)

  #list to find bullets that are not the player's bullets
  not_my_bullets = []
  #every bullet sprite in collision b
  for bu in collision_b:
    #see if bullet is the player's bullet
    if bu not in player.bullets:
      #appends to list
      not_my_bullets.append(bu)
      bullet_group.remove(bu)
      #find which player has this bullet and remove from its bullets group
      for p in player_list:
        if bu in p.bullets:
          p.bullets.remove(bu)
  
  #if there is collision
  if not player.immor and len(collision_a) !=0:
    player.lives -= 1
    #play sound
    ASTEROID_HIT_PLAYER_SOUND.play()
    if player.lives != 0:
      player.immor = True
      player.immor_count = time
    else:
      #if lives = 0
      player.die_respawn(time)
    a = collision_a[0] #collision is a list
    if a.rank > 1:
      #creates smaller sized asteroids
      a.destroy_respawn(a, WIDTH, HEIGHT, ASTEROID, asteroids)
    else:
      #create explosion 
      asteroid_explosion = explosion(a.x_pos, a.y_pos)
      asteroid_explosion.enter_q(time)

    return 1 #1 point deducted for every asteriod hit

  elif not player.immor and len(not_my_bullets) !=0:
    PLAYER_HIT_PLAYER_SOUND.play()
    player.lives -= 1
    #makes player immortal
    if player.lives !=0:
      player.immor = True
      player.immor_count = time
    else:
      #kills player
      player.die_respawn(time)
    #finds whos bullet it is
    for p in player_list:
      if not_my_bullets[0] in p.bullets:
        #removes bullet from bullet group
        p.bullets.remove(not_my_bullets[0])
        break

    return 3 #3 deducted for every collision with bullet

  #every power up that was collided
  for po in collision_p:
    player.rapid_fire = True
    player.bullet_interval = 60
    player.power_up_time = time

  return 0

def draw_window(current_time):
  '''
  main function to draw the window, so everything that is to be put on the window will be in this function

  Parameters:
    current_time: int
  
  Returns:
    None
  '''
  #puts the background as the image
  # timer(time, WIDTH/4, HEIGHT-10)
  #draws background
  WINDOW.blit(BACKGROUND, (0, 0))
  #moves and draws every asteroid created, and removes the ones that are off screen
  for a in asteroids:
    a.movement()
    a.draw(WINDOW)
    if a.check_off_screen(WIDTH, HEIGHT):
      asteroids.remove(a)
  #draws every explosion made
  for e in explosions_q:
    if current_time-e[1] < 500:
      e[0].draw(WINDOW)
    else:
      #removes explosion when the it has been on the screen long enough
      explosions_q.remove(e)
  #draws every power up made
  for p in power_up_group:
    if current_time-p.time < 3000:
      p.draw(WINDOW)
    else:
      #removes from group once the time limit is reached
      power_up_group.remove(p)

def play():
  '''
  function that runs the game
  
  parameters:
    None
  Returns:
    screen: int
    p1_score: int
    p2_score: int
  '''
  #pygame clock to track time
  clock = pygame.time.Clock()
  time = 0 
  # timer
  while 182-(time//1000) >= 0:
    #makes the game run at the FPS rate
    clock.tick(FPS)
    #get the time from clock
    time = pygame.time.get_ticks()
    #every 30 milliseconds create an asteroid
    if time %30 == 0:
      #gets random number for rank of asteroid
      ran = random.choice([1,1,1,2,2,3])
      #add new asteroid object to group
      asteroids.add(asteroid_obj(ran, WIDTH, HEIGHT, ASTEROID))
    
    #1/900 change for power up to pop up every millisecond
    r = random.randrange(1,900)
    if r == 1: 
      power_up_group.add(power_up(time))

    #this get_pressed from key tells us what keys are being pressed down, so look at all keys, and register it
    keys_pressed = pygame.key.get_pressed()
    #goes through player list
    for user in range(len(player_list)):
      if keys_pressed[pygame.K_ESCAPE]:
        return 1,0,0
      player_list[user].actions(keys_pressed, WINDOW, time)
      player_list[user].points += collision_group(player_list[user], asteroids, time)
      player_list[user].points -= player_collision_check(player_list[user], bullet_group, asteroids, power_up_group, time)

    #sets interval limit
    pygame.key.set_repeat(0,1)

    #loops through all the events that happen in the game
    for event in pygame.event.get():
      
      #if the even that the for loop received type is the same as the quit event
      if event.type == pygame.QUIT:
        #stops while loop
        break
    
    draw_window(time)
    #creates text for timer
    time_text = TIME_FONT.render(str(182-(time//1000))+ " seconds left", 1, WHITE)
    #draws time on screen
    WINDOW.blit(time_text, ((WIDTH//2)-(time_text.get_width()//2), 10))
    #interates through players
    for p in range(len(player_list)):
      ps = player_list[p]
      ps.power_up_timer(time)
      #draw player
      ps.draw(WINDOW, WIDTH, HEIGHT)
      #moves player
      ps.update_location(WIDTH, HEIGHT)
      #create text for player's health and points
      player_health = HEALTH_FONT.render("Health: " + str(ps.lives), 1, ps.colour)
      player_points = HEALTH_FONT.render("Points: " + str(ps.points),1, ps.colour)
      #draws text on screen
      WINDOW.blit(player_health, TEXT_POSITION[p])
      WINDOW.blit(player_points, (TEXT_POSITION[p][0], TEXT_POSITION[p][1]+30))
      #checks immor only when the player is immor to save time of checking every time
      if ps.immor:
        ps.immor_check(time)

      #update the display every loop
    pygame.display.update()
  return 4,player_list[0].points, player_list[1].points

  # pygame.quit()

def main():
  '''
  main function that runs the game

  Parameters:
    None

  Returns:
    None
  '''
  #-------------------------------------------------
  #Setting screen variable
  #1: home screen
  #2: how to play screen
  #3: play screen
  #-------------------------------------------------
  screen = 1
  #helps switch screens in game
  while True:
    if screen == 1:
      screen = home(WINDOW)
    elif screen == 2:
      screen = how_to_play(WINDOW)
    elif screen == 3:
      screen, p1_score, p2_score = play()
    elif screen == 0:
      pygame.quit()
    elif screen == 4:
      screen = win(WINDOW, p1_score, p2_score)
    elif screen == 5:
      screen = how_to_play_next(WINDOW)

#runs the main function only if this main file is being run
if __name__ == '__main__':
  main()