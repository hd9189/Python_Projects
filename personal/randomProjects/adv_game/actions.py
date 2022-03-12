import os

#use os.system("clear"), for every round of attacks by both sides

def fight(user, enemy):
  '''
  fight function simulates the fighting aspect of the game, when you die it gives you the choice to revive. Every round, it will give you the option to flee as well. The rewards system is also included if you've defeated a enemy.

  args:
    user: object
    enemy: object
    
  return:
    money_received: int
    is_new: bool
    leave: bool
  '''
  

  print()
  print(f"You've encountered a {enemy.name}\n")

  #this while loop lets you fight only once, so after the fight you continue on with the main code
  while True:
    choice = int(input("What would you like to do\n[1] Attack\n[2] Run\nChoice: "))
    while choice != 1 and 2:
      choice = int(input("Invalid input. What would you like to do?\n[1] Attack\n[2] Run\nChoice: "))
    os.system("clear")

    if choice == 1:
      user_damage = int(user.attack)
      enemy_health = int(enemy.health)
      enemy_health -= user_damage
      if enemy_health <= 0:
        money_received, revive_droplets = enemy.rewards_drop

        leave = input("Would you like to continue? [Y/N]: ")
        while leave.lower() != "y" and "n":
          leave = input("Invalid input. Would you like to continue? [Y/N]: ")
        if leave.lower() == "y": leave = True
        else: leave = False
        return money_received, revive_droplets, leave

      enemy_damage = enemy.attack
      user.health -= enemy_damage
      if user.health <= 0:
        if user.revive_droplets > 0:
          choice = user.revive
          if choice == "y":
            user.revive_droplets -= 1
            user.health = 100
            continue
        user.death
        return 0, 0, True

    elif choice == 2:
      print("You decided to flee")
      return 0, 0, True