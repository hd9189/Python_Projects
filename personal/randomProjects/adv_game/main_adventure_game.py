import locations
import os
import random
import sys
import actions

class player:

    def __init__(self, damage_range, health):
        '''
        This function initlizes a player object, where it defines the players customization to their character
        args:
          damage_range: list
          health: int
        '''
        #creating each attibute of object through inputs
        self.name = input("Please enter your username: ")
        self.gender = input("Please enter your preferred Gender [M] or [F]: ")
        #using inputs for invalid entries
        while self.gender.upper() != "M" and self.gender.upper() != "F":
            self.gender = input("Invalid try again. [M] or [F]: ")

        self.weapon = int(input("Please choose your weapon from this list: \n[1] Axe\n[2] Spear\n[3] Two Handed Sword\n[4] Two One-Handed Swords\nChoice: "))
        while self.weapon not in range(1,5):
            self.weapon = int(input("Invalid input try again \n[1] Axe\n[2] Spear\n[3] Two Handed Sword\n[4] Two One-Handed Swords\nChoice: "))
        if self.weapon == 1: self.weapon = "Axe"
        elif self.weapon == 2: self.weapon = "Spear"
        elif self.weapon == 3: self.weapon = "Two Handed Sword"
        elif self.weapon == 4: self.weapon = "Two One-Handed Swords"

        self.health = health
        self.damage_range = damage_range
        self.money = 5000
        self.ores_accquired = 0
        self.revive_droplets = 0
        self.is_alive = True

    def teleport(self):
      '''
      This is the teleport function for the user object, so they can go to different floors or places in the game
      '''
      print()
      for x in range(len(teleport_places)): 
          print(f"[{x}]: {teleport_places[x]}")
      place = input("Please input where you want to go now: ")
      return place

    def attack(self):
      '''
      attack action for the player object, using random to determine a random damage range
      
      return:
        damage: int
      '''
      print()
      damage = random.randint(self.damage_range[0], self.damage_range[1])
      print(f"You have dealt {damage} to the enemy")
      return damage
      #self note: don't forget to have a death fucntion, so you can use revival items if needed

    def revive(self):
      print()
      '''
      In case of death of the character, if they have a revive dropley they could use, then this function helps them use it 
      
      return:
        choice: str
      '''
      choice = input("You can use a revival droplet would you like to use it? [Y/N] : ").lower()
      while choice != "y" and "n":
        choice = input("Invalid input. Would you like to use it? [Y/N] : ")
      
      return choice

    def death(self):
      '''
      this function is when the player dies, it will do this to respawn the player
      '''
      print()
      self.money = self.money//3
      self.ores_acquired = self.ores_acquired//2
      self.is_alive = False
      print(f"You have died, you will be respawned again. You have {self.money} now, and {self.ores_acquired} ores now.")
      
      
#creating a class for all enemies, including bosses and hunting ground monsters
class enemy:
  
  def __init__(self, health, damage_range, attack_method, name, reward, is_boss):
    '''
    initializing the attributes for the enemy object
    args:
      health: int
      damage_range: list
      attack_method: str
      name: str
      reward: (money) list
      is_boss: bool
    '''
    self.health = health
    self.damage_range = damage_range
    self.attack_method = attack_method
    self.name = name
    self.reward = reward
    self.is_boss = is_boss

  def attack(self):
    print()
    '''
    attacking action for the enemy object

    return:
      damage: int
    '''
    damage = random.randint(self.damage_range[0], self.damage_range[1])
    print(f"{self.name} has just {self.attack_method} you.")
    print(f"{damage} has been dealt to you")
    return damage

  def rewards_drop(self):
    print()
    '''
    rewards drop function for the enemy, and if the enemy is a boss, then theres a chance to drop elucidator or revival 

    return:
      reward: int
      revive_drop: int
    '''
    print(f"Yay! You defeated the {self.name}")
    reward = random.randint(self.reward[0], self.reward[1])
    print(f"{self.name} dropped ${reward}")
    if self.is_boss:
      revive_drop = random.randint(0,1)
      if revive_drop == 1:
        print(f"{self.name} dropped a revivale droplet, if you die you can consume it and be revived to full health.")
    #this else is here so that if the enemy is not a boss, the function can still return a value for revive_drop
    else:
      revive_drop = 0
      return reward, revive_drop
    

#to create different scenarios 
new_location = {"big door": True, "Shop": True, "Floor 1": True, "Hunting Grounds": True}
companions = []
teleport_places = ["Quit Game", "Big door", "Floor 1", "Floor 24", "Floor 48", "Floor 74", "Floor 75", "Shop"]
items_collected = []
ores_accquired = 0
final_fight = False

#list of enemies for hunting grounds depending on floors
floor1_enemies = [
  [15, [5,8], "tackled", "Frenzy Boar", 2, False],
  [10, [4,6], "bit", "Little Nepents", 1, False],
  [25, [5,10], "bit", "Large Nepents", 5, False],
  [17, [7,9], "slapped", "Scavenger Toads", 4, False],
  [30, [10, 13], "scratched", "Dire Wolf", 10, False]
  ]

#creates the user object, which is the player
user = player([5,10], 100)

#first initiates the game, so that everytime the while loop, loops back it won't activate the big door function
new_to, fight = locations.big_door(items_collected, companions, new_location["big door"], user)
new_location["big door"] = new_to
final_fight = fight

while not final_fight:
    user.health = 100
    user.is_alive = True
    #variable for the desired location to be teleported to, then use if statements to activate the certain location functions depending on where they want to go
    desired_location = int(user.teleport())

    if "Hunting Ground" in teleport_places and desired_location not in [2,3,5,6,8]:
      teleport_places.remove("Hunting Ground")

    #this while loop is in case the input is invalid
    while desired_location not in range(len(teleport_places)):
        print("invalid input")
        desired_location = int(user.teleport())

    if desired_location == 0:
      print("Thanks for playing the game! Come back Again.")
      sys.exit()

    elif desired_location == 1:
        os.system('clear')
        new_to, fight = locations.big_door(items_collected, companions, new_location["big door"], user)
        new_location["big door"] = new_to
        final_fight = fight

    elif desired_location == 2:
        if new_location["Floor 1"]:
          companion, new_to = locations.floor_1(user, new_location["Floor 1"])
          if companion == "Klein":
            print("\nYou have a new companion: Klein\n")
            companions.append(companion)
          monster = enemy(floor1_enemies[0][0], floor1_enemies[0][1], floor1_enemies[0][2], floor1_enemies[0][3], floor1_enemies[0][4], floor1_enemies[0][5])

          money_gained, is_new = actions.fight(user, monster)
          print("Klein: Man that was fun! Thanks for teaching me so much stuff, I feel like I'll be able to solo a boss now! Anyways thanks! See you later!")
          user.money += money_gained
          new_location["Hunting Grounds"] = is_new
          new_location["Floor 1"] = new_to

        else:
          companion, new_to = locations.floor_1(user, new_location["floor 1"])
        teleport_places.append("Hunting Grounds [floor 1]")

    elif desired_location == 7:
        new_location["Shop"], new_companion, money_left, ores_bought, weapon = locations.shop(new_location["Shop"], user.money, user)
        if new_companion == "Agil":
            print("\nYou have a new companion: Agil\n")
            companions.append(new_companion)
        money = money_left
        print(f"\nYou have ${money}\n")
        user.ores_accquired += ores_bought
        if weapon != "":
            user.weapon = weapon
            print(f"Your weapon is now {user.weapon} Congrats!\n")
            user.damage_range = [7,15]

    elif desired_location == 8:
      if teleport_places[desired_location] == "Hunting Grounds [floor 1]":
        while True:
          enemy_num = random.randint(0, len(floor1_enemies)-1)
          moster = enemy(floor1_enemies[enemy_num][0], floor1_enemies[enemy_num][1], floor1_enemies[enemy_num][2], floor1_enemies[enemy_num][3], floor1_enemies[enemy_num][4], floor1_enemies[enemy_num][5])
          money_received, is_new, leave = locations.hunting_grounds(user, monster, new_location["Hunting Grounds"])
          if leave:
            print("You left the hunting grounds")
            break
