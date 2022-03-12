import os
import actions
import random

def big_door(items, companions, new, user):
  os.system("clear")
  '''
  This function is the start of the game, and the point where the player must return to once they have gathered all their items, to defeat the final boss"

  Args:
    items: list(str)
    companions: (list(str))
    new: boolean

  return:
    new: boolean
    can_enter_bossroom: boolean
  '''

#if the player is new to this location
  if new:
    print(f"Guard: Hello {user.name} welcome to Sword Art Online or Aincrad. We have been trapped in Akihiko Kayaba's VRMORPG game, and we must beat the game to escape. Behind this large door is the final boss that the players must beat, however, as the guard keeper I will let anyone in without the things needed to defeat the boss. There is the Elucidator dropped by any random boss, Dark Repluser that can only be forged by the finest blacksmith, and the long lost skill: Dual Wieding. Go collect these and once you have I will accompany you to escape this retched game.")
    return False, False

#if player is not new to the location, but does not have the items to complete quest
  elif not new and len(items) != 3:
    print("Guard: Back so soon? you don't even have the three things yet! Make haste, There are mroe and more people giving up on beating this game. Their losing hope......")
    return False, False

#if player is not new and has all three items
  elif not new and len(items) == 3:
    print(f"Guard: You've finally done it! Well done. lets go in, and defeat that boss. I'm so sick of staying in this game. I see that you have brough {companions} with you, that is reassuring.")
    return False, True

#dictionary to indicate the items in shop, and their cost
items_in_shop = {
    "Night Sky weapon": 100,
    "Weapon forging ores": 500,
}
def shop(new, money, user):
    os.system("clear")
    '''
    This function is a place called shop, where the player can go to the shop to buy a weapon and ores, the ores are required to forge a necessary weapon 

    args: 
    new: boolean
    money: int
    user: object

    return:
    new_location["Shop"]: boolean
    new_companion: str
    current_balance: int
    ores_bought int
    weapon: str
    '''
    if new:
        print("Agil: Hey there! Welcome to the Egiru no Mise, our motto is buy cheap sell cheap. I've never seen you before, you must be new. Let me introduce myself, I'm Agil a shopkeeper and a axe user. I'm part of the assault team, so I'd say I'm pretty storng. What might you be looking for\n\nOh! Your the new rookie everyones been talking about? I see, well whenever you need help or whenever you or your buddies finally get the chance to go into the blasted big door, then give me a holler and I'll come straight to you.\n\nCome back again!")
        return False, "Agil", money, 0, ""
    
    print(f"Balance: {money}\n")
    print("Agil: So what are you here for today?\n")
    for item, price in items_in_shop.items():
        print(f"{item}: ${price}")
    
    print("\ntype 0 to leave\n")
    buy = input("input what you would like (one item per visit): ")
    while buy != "0" and buy not in items_in_shop.keys():
      buy = input("input what you would like (one item per visit): ")
    if buy == "0":
        print("you have left the shop")
        return False, "", money, 0, ""
    #if the user buys a weapon, some new things have to be returned
    elif buy == "Night Sky weapon":
        if money < items_in_shop[buy]:
            print("You don't have enough money kid. Come back when you have more.")
            return False, "", money, 0, ""
        else:
            print("Nice doing business with you")
            money -= items_in_shop[buy]
            return False, "", money, 0, f"Night Sky {user.weapon}"
    else:
        quantity = int(input(f"How many {buy} would you like to buy: "))
        if items_in_shop[buy]*quantity > money:
            print("You don't have enough money kid. Come back when you have more.")
            return False, "", money, 0, ""
        else:
            print("Nice doing business with you")
            money -= items_in_shop[buy]*quantity
            return False, "", money, quantity, ""

def floor_1(user, new):
  os.system("clear")
  '''
  This function is when the user decides to teleport to floor 1 of the game. it lets you meet a new companion, and also gives you the option to either go into the secret labyrinth or you can to hunt and farm in the hunting ground

  args:
    user: object
    new: bool

  return:
    companion: str
    new: bool
  '''

  if new:
    print("You've arrived at the first floor of Aincrad [The town of beginnings]. Where the players first discovered that they were fated to either win or die within this game. This is the place where the depression began.......")
    print("\nA man sudden walks up to you\n")
    print(f"Klein: Hi there! Are you the new rookie that everyones talking about? {user.name}, it really is you! Say I'm quite a beginner of this game, even though all of this here have been stuck in this game for a while now... Anyways! Could you show me a few moves, and give me some tips?")
    choice = input("[1] Sure I'd love to, lets go to the hunting grounds!\n[2] Sorry I'm kinda busy.\nRespoonse: ")
    while choice != "1" and choice != "2":
      choice = input("Invalid Input\n[1] Sure I'd love to, lets go to the hunting grounds!\n[2] Sorry I'm kinda busy.\nResponse: ")
    
    if choice == "1":
      print("Alright sweet! I knew you were a nice person. Lets go to the hunting grounds!")

    elif choice == "2":
      print("Aww don't be like that. Come on lets go!")

    print("\nYou and Klein both go to the [hunting grounds] togehter")
    return "Klein", False

  else:
    print("[You've arrived in floor 1]\n\n")
    speech = random.randint(1,3)
    if speech == 1:
      print(f"Klein: Oh, {user.name} your here again! Where you going?")
    elif speech == 2:
      print(f"Whatsup {user.name}? Hows it going man, guess what? I leveled up! Isn't it amazing? It's all thanks to your tips. I got a clan I lead now, I'm so strong thanks to you helping me get jumpstarted!")
    else:
      print("Yo, crazy bumping into you here. I just dropped by, I went up a few floors now, I live on flor 50, if your ever there visit me, you've helped me so much after all its the least I could do.")

    return "", False

def hunting_grounds(user, enemy, new):
  os.system("clear")
  '''
  This function is for the hunting grounds on certain floors, using the fight function from the actions files to simulate a fight, in the main function there will be a while loop to simulate a continuous fight with different monsters 

  args:
    user: object
    enemy: object
    new: bool
  '''

  if new:
    print("Welcome to the hunting grounds! This is where you can farm monsters and earn some more money! Be careful, as the higher tthe floor you are at the stronger the monsters are. In the hunting ground, it's always 1v1 with you and the monster take turns sriking each other. This is the same with boss monsters that you would encounter in boss rooms. However boss's might drop the item your looking for the [Elucidator] or they could drop a [Revive droplet] which could revive you to full health when you die. You have the option to flee if you think you won't be able to handle it! Good luck, and happy hunting!")

  money_received, revive_droplets, leave = actions.fight(user, enemy)
  return money_received, revive_droplets, leave
  