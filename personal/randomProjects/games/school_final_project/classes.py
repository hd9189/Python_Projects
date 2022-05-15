import pygame
import math
import random

bullet_group = pygame.sprite.Group()
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
    self.lives = 3
    self.immor = False
    self.fire_sound = fire_sound


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
    pygame.draw.rect(WINDOW, (255,0,0), self.rect, 2)
    #draws the bullets
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
    self.rotate_surf = pygame.transform.rotate(self.image, self.angle)
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
    if self.x_pos > WIDTH: self.x_pos = 1
    #use elif to skip additional checking
    elif self.x_pos < 0: self.x_pos = WIDTH-1
    if self.y_pos > HEIGHT: self.y_pos = 1
    elif self.y_pos < 0: self.y_pos = HEIGHT-1

  def die_respawn(self):
    pass


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
    self.rect = pygame.draw.rect(WINDOW, self.colour, [self.x, self.y, self.w, self.h])

  def check_off_screen(self, WIDTH, HEIGHT):
    '''
    function to check if the bullet is off screen, if it is delete it, because it could should asteroids out of the screen, and also wastes space

    parameter:
      WIDTH: width of window
      HEIGHT: height of window
    '''
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
    #self.hit_box_range = (self.x_pos, self.y_pos, self.width, self.height) #hit box rectangle position and dimension
    #self.rect = pygame.draw.rect(WINDOW, (255,0,0), self.hit_box_range, 2) #hit box
    #self.angle = 0
    self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))

  def movement(self):
    '''
    moves the asteroid every frame
    
    Parameters:
      self: asteroid object itself with its attributes

    Returns:
      None
    '''
    #self.angle += 5
    #self.img = pygame.transform.rotate(self.img, self.angle)
    self.x_pos += self.x_vel
    self.y_pos += self.y_vel
    # self.hit_box_range = (self.x_pos, self.y_pos, self.width, self.height)
    #self.rect = pygame.draw.rect(WINDOW, (255,0,0), self.hit_box_range, 2) #hitbox
    self.rect = self.img.get_rect()
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
    #pygame.draw.rect(WINDOW, (255,0,0), self.hit_box_range, 2) #hitbox
  
  def check_off_screen(self, WIDTH, HEIGHT):
    '''
    checks if the asteroid is too off screen, returning true if it is so it can be deleted
    
    Parameters:
      self: object
      WIDTH: window width
      HEIGHT: width height
    
    Returns:
      destroy: bool'''
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
