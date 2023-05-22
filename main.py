import os
import time
import random

# Github check

# ANSI escape code list
# Normal Colors
BLACK = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[94m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright Colors
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"



RESET = "\033[0m"

# Player stats
player_health = 100
attack_speed = 1000
attack_delay_seconds = attack_speed / 1000.0
inventory_slots = 20
money = 0
flight_speed = 0
can_fly = False
level = 0
xp = 0

# Inventory
player_inventory = ["Torch", "Sword", 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Print only the items in the inventory
# Use a list comprehension to iterate over the elements of player_inventory
# and filter out non-item elements (numbers or other non-string values)
# by checking if each element is of type str using the isinstance() function.
# The resulting list contains only the item names.
filtered_inventory = [item for item in player_inventory if isinstance(item, str)]

found_items = ["Shield", "Leather Helmet", "Leather Chestplate", "Leather Pants", "Leather Boots"]

for item in found_items:
    if None in player_inventory:
        slot = player_inventory.index(None)
        player_inventory[slot] = item
        print("Item", item, "Added To Slot", slot+1)
    else:
        print("Inventory Is Full, Unable To Add Item")

# Level logic
# This is a list use xp_levels[0-9] to get it
#xp_levels = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]

# This is a dictionary use xp_levels[1-10] to get them
xp_levels = {
    1: 100,
    2: 200,
    3: 400,
    4: 800,
    5: 1600,
    6: 3200,
    7: 6400,
    8: 12800,
    9: 25600,
    10: 51200
}

def add_item_to_inventory(item):
    global filtered_inventory
    
    player_inventory.append(item)
    filtered_inventory = [item for item in player_inventory if isinstance(item, str)]
    print("Item", item, "Added To Your Inventory")

def check_level_up():
    global level
    for lvl, xp_threshold in xp_levels.items():
        if xp >= xp_threshold:
            level = lvl

def shop():
    print(CYAN + "Shop Items And Prices: " + RESET)
    print(" ")
    print(MAGENTA + "Speed ~ $50")
    print("Strength ~ $50")
    print("Damage ~ $500")
    print("Attack Speed ~ $750")
    print("Movement Speed ~ $750")
    print("Flight ~ $1000" + RESET)
    
    if can_fly:
        print("Flight Speed ~ $500")
    
def player_info():
    global player_inventory
    
    print("Player Stats")
    print("____________") 
    print(" ")
    
    print(YELLOW + "Player Health: " + RESET, player_health)
    print(YELLOW + "Attack Speed: " + RESET, attack_speed)
    print(YELLOW + "Inventory Slots: " + RESET, inventory_slots)
    print(YELLOW + "Money: " + RESET, money)
    print(YELLOW + "Current Level: " + RESET, level)
    
    if can_fly:
        print(YELLOW + "Flight Speed: " + RESET, flight_speed)
      
    print("Player Inventory:", filtered_inventory)
        
    player_info_main_menu = input(RED + "Type 1 To Go Back To The Main Menu: " + RESET)
    
    if player_info_main_menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu()
    
def credits():
    print("Developer: StinkyBagel")
    
    back = input(RED + "Type 1 To Go Back To The Menu: ")
    
    if back == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu()

def game_info():
    print(BRIGHT_GREEN + "The premise of the game is to fight enemies and gain xp and money.")
    print("You can use the money to buy upgrades in the shop." + RESET)
    
    back = input(RED + "Type 1 To Go Back To The Menu: ")
    
    if back == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu()

def main_menu():
    # global allows to be accessed and modified from different functions
    global player_health
    global attack_speed
    global inventory_slots
    global money
    global xp
    global found_items
    
    print(BLUE + "   _____ _                          _               _____ _           _     " + RESET)
    print(BLUE + "  / ____| |                        | |             / ____| |         | |    " + RESET)
    print(BLUE + " | |    | |__   __ _ _ __ __ _  ___| |_ ___ _ __  | |    | | __ _ ___| |__  " + RESET)
    print(BLUE + " | |    | '_ \ / _` | '__/ _` |/ __| __/ _ \ '__| | |    | |/ _` / __| '_ \ " + RESET)
    print(BLUE + " | |____| | | | (_| | | | (_| | (__| ||  __/ |    | |____| | (_| \__ \ | | |" + RESET)
    print(BLUE + "  \_____|_| |_|\__,_|_|  \__,_|\___|\__\___|_|     \_____|_|\__,_|___/_| |_|" + RESET)

    print(" ")
    print(GREEN + "1.) Shop, 2.) Player Info, 3.) Credits, 4.) Game Info, 5.) Get More Stats And Equipment (remove before releasing)" + RESET)
    print(" ")

    title_options = input(RED + "Pick One: " + RESET)

    if title_options == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        shop()
    elif title_options == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        player_info()
    elif title_options == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        credits()
    elif title_options == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        game_info()
    elif title_options == "5":
        player_health += 5
        attack_speed += 5
        inventory_slots += 5
        money += 5
        xp += 51200
        debug_found_item = found_items[:2]
        add_item_to_inventory(debug_found_item[0])
        add_item_to_inventory(debug_found_item[1])
        check_level_up()
        os.system('cls' if os.name == 'nt' else 'clear')
        player_info()
    
    
main_menu()