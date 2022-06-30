import pygame
import math
import random
import os

bullet_group = pygame.sprite.Group()
explosion_img = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'explosion.png')), (25,25))
power_img = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'power_up.png')), (25,50))
  
explosions_q = []
#-------------------------------------------------
#class for the player
#-------------------------------------------------
class player():
  '''
  Class that creates the playable character, along with the different functions that the player can do

  Attributes:
    image: image of the player, what they are displayed as on the screen
    colour: colour theme of the image, a RGB tuple
    points: int value representing the amount of points collected by the player
    width: int value of the width of avatar/image
    height: int value of the height of avatar/image
    x_pos: int value of the horizontal position of the player on the screen
    y_pos: int value of the vertical position of the player on the screen
    contorls: list of the specific controls the user uses to contorl the avatar
    angle: int value of the angle the player is rotated at
    rotated_surf: the image but rotated
    rect: rectangle of the rotated avatar
    rect.center: center value of the rectangle of avatar, a pygame.Rect function
    cosine: cosine value of the angle the avatar is rotated at
    sine: sine value of the angle the avatar is rotated at
    head: x and y position of the head of avatar
    bullets: sprite group of the bullets that the player fired
    last_fired: int value acting as a interval tracker to limit bullet spamming
    lives: int value representing number of lives left till dying
    immortal: bool value indicating if the user is currently immortal (meaning that nothing will take a life)
    fire_sound: file from assets folder
    bullet_interval: interval in which bullets can be fired
    rapid_fire: bool value to indicate the state of player, if they are power up or not
    power_up_time: int value indicating the time when the player just got the power up
  '''
  #set the variables and attributes for the user
  def __init__ (self, pos, player_img, colour, controls, fire_sound):
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
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.x_pos = pos[0]
    self.y_pos = pos[1]
    self.init_pos = (pos[0], pos[1])
    #0: left, 1: right, 2: up, 3: down
    self.controls = controls
    self.angle = 0
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    
    self.rect = self.rotate_surf.get_rect()
    self.rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    #get coordinates of the head of the image
    self.head = (self.x_pos + self.cosine + self.width//2, self.y_pos - self.sine*self.height//2)
    self.bullets = pygame.sprite.Group()
    self.last_fired = 0
    self.points = 0
    self.lives = 5
    self.immor = False
    self.immor_count = 0
    self.fire_sound = fire_sound
    self.bullet_interval = 120
    self.rapid_fire = False
    self.power_up_time = 0


  #function to help put the 
  def draw(self, WINDOW, WIDTH, HEIGHT):
    '''
    puts the players on the window during the game and every update of screen. Also redraws every bullet but after it was moved

    parameters:
      self: the object itself
      WINDOW: the window where everything is drawn on
      WIDTH: int value of the window width
      HEIGHT: int value of the window height

    Returns:
      None
    '''
    WINDOW.blit(self.rotate_surf, self.rect)
    if self.immor:
      #draws rect around user if immortal
      pygame.draw.rect(WINDOW, self.colour, self.rect, 2)
    if self.rapid_fire:
      #draws a circle around user to indicate power up
      pygame.draw.circle(WINDOW, (0,255,0), self.rect.center, 50, width=2)
    #iterates through the players bullets and draws them
    for bullet in self.bullets:
      bullet.move()
      bullet.draw(WINDOW)
      if bullet.check_off_screen(WIDTH, HEIGHT):
        self.bullets.remove(bullet)

  def turnLeft(self):
    '''
    function to change the angle of which the user is facing when specific key is pressed

    Parameters:
      self: object itself

    Returns:
      None
    '''
    self.angle += 5
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    self.rect = self.rotate_surf.get_rect()
    self.rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    self.head = (self.x_pos + self.cosine * self.width//2, self.y_pos - self.sine*self.height//2)

  def turnRight(self):
    '''
    function to change the angle of which the user is facing when specific key is pressed

    Parameters:
      self: object itself

    Returns:
      None
    '''
    self.angle -= 5
    #rotate the image
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    #roate rect
    self.rect = self.rotate_surf.get_rect()
    self.rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    self.head = (self.x_pos + self.cosine * self.width//2, self.y_pos - self.sine*self.height//2)
    
    
  def moveForward(self):
    '''
    function to make the avatar move forward when forward key is pressed

    Parameters:
      self: object itself

    Returns:
      None
    '''
    self.x_pos += self.cosine*5
    self.y_pos -= self.sine*5
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    self.rect = self.rotate_surf.get_rect()
    self.rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    self.head = (self.x_pos + self.cosine * self.width//2, self.y_pos - self.sine*self.height//2)

  def moveBackward(self):
    '''
    function to make the avatar move backward when specific key is pressed
    
    Parameters:
      self: object itself

    Returns:
      None
    '''
    self.x_pos -= self.cosine*5
    self.y_pos += self.sine*5
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
    self.rect = self.rotate_surf.get_rect()
    self.rect.center = (self.x_pos, self.y_pos)
    #get direction of where the player is facing
    self.cosine = math.cos(math.radians(self.angle + 90))
    self.sine = math.sin(math.radians(self.angle + 90))
    self.head = (self.x_pos + self.cosine * self.width//2, self.y_pos - self.sine*self.height//2)

  def actions(self, keys_pressed, WINDOW, time):
    '''
    function to activate each moving function if a specific key of the player is pressed
    
    Parameters:
      self: player object itself
      keys_pressed: list of the personalized keys for the player to move
      WINDOW: screen for the game
      time: int value of the current time in the game
      
    Returns:
      None
    '''
    #runs functions depending on what keys are pressed
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
      if time-self.last_fired >=self.bullet_interval:
        new_bullet = bullet(self, WINDOW)
        self.fire_sound.play()
        new_bullet.draw(WINDOW)
        self.bullets.add(new_bullet)
        self.last_fired = time
        bullet_group.add(new_bullet)

  def update_location(self, WIDTH, HEIGHT):
    '''
    function to move the player if they go off screen

    Parameters:
      self: player object
      WIDTH: int value of the width of screen
      HEIGHT: int value of the width of screen
      
    Returns:
      None
    '''
    #lets user not run out of the screen
    if self.x_pos > WIDTH: self.x_pos = 1
    #use elif to skip additional checking
    elif self.x_pos < 0: self.x_pos = WIDTH-1
    if self.y_pos > HEIGHT: self.y_pos = 1
    elif self.y_pos < 0: self.y_pos = HEIGHT-1

  def immor_check(self,current_time):
    '''
    checks if the player should still be immortal

    Parameters:
      self: object
      current_time: int value of time in game
    '''
    #checks how long the player has been immortal
    if current_time - self.immor_count > 2000: #2 seconds
      self.immor = False
      self.immor_count = 0

  def die_respawn(self, time):
    '''
    kills player and relocates them after they lose all health

    parameters:
      self: object
      time: current time in game
    '''
    #resets position of user and all status
    self.immor = True
    self.immor_count = time
    self.x_pos = self.init_pos[0]
    self.y_pos = self.init_pos[1]
    self.angle = 0
    self.lives = 5

  def power_up_timer(self, time):
    #finds time on how long the player had the power up
    if time - self.power_up_time > 5000:
      self.bullet_interval = 120
      self.rapid_fire = False


class bullet(pygame.sprite.Sprite):
  '''
  class that creates a bullet object for player to fire

  Attributes:
    point: tuple of coordinates for the front of the avatar
    x,y: x and y coordinates of point
    w: width of bullet
    h: height of bullet
    c = cosine angle value of player
    s = sine angle value of player
    xvelocity: how much the bullet should move horizontally, when angle is taken into consideration
    yvelocity: how much the bullet should move vertically, when angle is taken into consideration
    rect: a rectangle to represent the bullet itself
    colour: colour of bullets the same as the colour of the avatar, tuple in RGB values
  '''
  def __init__(self, player, WINDOW):
    '''
    initialize and set the values for bullet attributes

    Parameters:
      self: object itself
      player: player object, since the bullets are personalized towards that specific person
      WINDOW: the window screen
    '''
    #call the parent class sprite constructor, making the object a sprite
    pygame.sprite.Sprite.__init__(self)
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
    self.colour = player.colour
    self.rect = pygame.draw.rect(WINDOW, self.colour, [self.x, self.y, self.w, self.h])

  def move(self):
    '''
    moves the bullet by changing the position
    
    Parameters:
      self: bullet object itself
    
    Returns:
      None
    '''
    self.x += self.xvelocity
    self.y -= self.yvelocity

  def draw(self, WINDOW):
    '''
    draws the bullet on screen

    parameters:
      WINDOW: window itself

    returns:
      None
    '''
    #draws bullet
    self.rect = pygame.draw.rect(WINDOW, self.colour, [self.x, self.y, self.w, self.h])

  def check_off_screen(self, WIDTH, HEIGHT):
    '''
    function to check if the bullet is off screen, if it is delete it, because it could should asteroids out of the screen, and also wastes space

    parameter:
      WIDTH: width of window
      HEIGHT: height of window
    '''
    #checks if bullet is off screen
    if self.x < -1 or self.x > WIDTH or self.y <-1 or self.y > HEIGHT:
      return True

class asteroid_obj(pygame.sprite.Sprite):
  '''
  class to define the asteroid objects that the player can shoot down

  Attributes:
    rank: int value that is randomly determined to determine the size of asteroid
    img: the image of the transformed asteroid according to size
    rpoint: determines random point of where the asteroid should be created in the window
    x_pos, y_pos: x and y position of rpoint
    x_dir, y_dir: direction of the way the asteroid should move along the x and y axis
    x_vel, y_vel: velocity of the asteroid for x and y
    rect: hitbox of the asteroid
  '''
  def __init__(self, rank, WIDTH, HEIGHT, ASTEROID):
    '''
    function to initialize the object and assign values to its attributes

    Parameters:
      self: asteroid object itself
      rank: int value to determine size
      WIDTH: width of screen
      HEIGHT: height of screen
      ASTEROID: asteroid image

    Returns:
      None
    '''
    pygame.sprite.Sprite.__init__(self)
    self.rank = rank
    #decides image size depending on rank
    if self.rank == 1: self.height, self.width = (25,25) #small size
    elif self.rank == 2: self.height, self.width = (50,50) #medium size
    elif self.rank == 3: self.height, self.width = (75,75) #large size
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
    self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))

  def movement(self):
    '''
    moves the asteroid every frame
    
    Parameters:
      self: asteroid object itself with its attributes

    Returns:
      None
    '''

    self.x_pos += self.x_vel
    self.y_pos += self.y_vel
    #self.rect is attribute needed for collision function
    self.rect = self.img.get_rect()
    #asteroid hitbox
    self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))
    

  def draw(self, WINDOW):
    '''
    draws the asteroid every frame onto the window

    Parameters:
      self: object attributes
      WINDOW: the screen

    Returns: 
      None
    '''
    WINDOW.blit(self.img, (self.x_pos, self.y_pos))
  
  def check_off_screen(self, WIDTH, HEIGHT):
    '''
    checks if the asteroid is too off screen, returning true if it is so it can be deleted
    
    Parameters:
      self: object
      WIDTH: window width
      HEIGHT: width height
    
    Returns:
      destroy: bool
    '''
    if self.x_pos < -70 or self.x_pos > WIDTH+4 or self.y_pos <-70 or self.y_pos > HEIGHT+4:
      return True

  def destroy_respawn(self, a, WIDTH, HEIGHT, ASTEROID, asteroids):
    '''
    if the asteroid is hit, it removes itself from the group and generates smaller asteroids from it

    Parameters:
      a: asteroid object
      WIDTH: width of screen
      HEIGHT: height of screen
      ASTEROID: asteroid image
      asteroids: sprite group of the asteroids on screen

    returns:
      None
    '''
    ran = random.randrange(2,4)
    for x in range(ran):
      new_asteroid = asteroid_obj(a.rank-1, WIDTH, HEIGHT, ASTEROID)
      new_asteroid.x_pos = a.x_pos
      new_asteroid.y_pos = a.y_pos 
      asteroids.add(new_asteroid)

class explosion():
  '''
  class to define the explosion of asteroids after being destroyed

  Attributes:
  img: a file from assets
  pos: a tuple of the position of asteroid when destroyed
  '''
  def __init__ (self,x,y):
    '''
    Parameters:
      self: the object
      x: int value of x position
      y: int value of y position
    
    Returns:
      None
    '''
    self.img = explosion_img
    #position of asteroid
    self.pos = (x,y)
  def draw(self, WINDOW):
      '''
      Draws the explosion image at the position on window
      Parameters
        self: object
        WINDOW: the window of the game

      '''
      WINDOW.blit(self.img, self.pos)
  def enter_q(self, time):
    '''
    Function that enters the explosion and time of explosion to a queue (list)

    Parameters:
      self: object
      time: int
    Returns:
      none
    '''
    #enters list and once it reaches the 3 second time limit it is removed from queue
    explosions_q.append((self, time))

class power_up(pygame.sprite.Sprite):
  '''
  class to create power up images in game

  Attributes:
    x: random int value
    y: random int value
    W: int width of rect
    H: int width of rect
    duration: int value to indicate how long the bullet should stay for
    img: image
    rect: pygame rect
    time: int value of time
  '''

  def __init__(self, time):
    '''
    initialize the sprite

    Parameters:
      self: object
      time: int value

    Returns:
      None
    '''
    pygame.sprite.Sprite.__init__(self)

    self.x = random.randrange(10, 990)
    self.y = random.randrange(10, 740)
    self.W = 15
    self.H = 30
    self.duration = 5
    self.img = power_img
    self.rect = pygame.Rect((self.x, self.y), (self.W, self.H))
    self.time = time

  def draw(self, WINDOW):
    '''
    draws the image at a random spot
    
    Parameters:
      self: object
      WINDOW: pygame window

    Returns:
      None
    '''
    #draws image
    WINDOW.blit(self.img, (self.x, self.y))