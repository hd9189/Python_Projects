import pygame
import math
import random
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
    self.bullets = pygame.sprite.Group()
    self.last_fired = 0


  #function to help put the 
  def draw(self, WINDOW, WIDTH, HEIGHT):
    '''
    puts the players on the window during the game and every update of screen
    '''
    WINDOW.blit(self.rotate_surf, self.rotated_rect)
    #draws the bullets
    for bullet in self.bullets:
      bullet.move()
      bullet.draw(WINDOW)
      if bullet.check_off_screen(WIDTH, HEIGHT):
        self.bullets.remove(bullet)

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
        self.bullets.add(new_bullet)
        self.last_fired = time

  def update_location(self, WIDTH, HEIGHT):
    if self.x_pos > WIDTH: self.x_pos = 1
    #use elif to skip additional checking
    elif self.x_pos < 0: self.x_pos = WIDTH-1
    if self.y_pos > HEIGHT: self.y_pos = 1
    elif self.y_pos < 0: self.y_pos = HEIGHT-1

  def collision():
    pass

  def die_respawn():
    pass


class bullet(pygame.sprite.Sprite):
  def __init__(self, player):
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

  def move(self):
    self.x += self.xvelocity
    self.y -= self.yvelocity

  def draw(self, WINDOW):
    pygame.draw.rect(WINDOW, (255,255,255), [self.x, self.y, self.w, self.h])

  def check_off_screen(self, WIDTH, HEIGHT):
    if self.x < -1 or self.x > WIDTH or self.y <-1 or self.y > HEIGHT:
      return True


# def timer(text, x, y):
#   img = TIMER_FONT.render(text, True, WHITE)
#   WINDOW.blit(img, (x,y))

class asteroid_obj(pygame.sprite.Sprite):
  def __init__(self, rank, WIDTH, HEIGHT, ASTEROID):
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
    self.hit_box_range = (self.x_pos, self.y_pos, self.width, self.height) #hit box rectangle position and dimension
  def movement(self):
    self.x_pos += self.x_vel
    self.y_pos += self.y_vel
    self.hit_box_range = (self.x_pos, self.y_pos, self.width, self.height)

  def draw(self, WINDOW):
    WINDOW.blit(self.img, (self.x_pos, self.y_pos))
    pygame.draw.rect(WINDOW, (255,0,0), self.hit_box_range, 2)
  
  def check_off_screen(self, WIDTH, HEIGHT):
    if self.x_pos < -70 or self.x_pos > WIDTH+4 or self.y_pos <-70 or self.y_pos > HEIGHT+4:
      return True