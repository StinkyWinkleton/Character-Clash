import os
import time
import random
import tkinter as tk

# Create window
window = tk.Tk()

canvas_size = 1000

# Create canvas
canvas = tk.Canvas(window, width = window.winfo_screenwidth(), height = window.winfo_screenheight())
canvas.pack()

center_y = canvas_size // 2
center_x = canvas_size // 2

window.geometry(f"{canvas_size}x{canvas_size}")

def display_text(text):
    canvas.create_text(center_x, center_y, text = text, font = ("Arial", 16), fill = "black")

# Github check

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
        display_text("Item", {item}, "Added To Slot", {slot+1})
    # else:
        # display_text("Inventory Is Full, Unable To Add Item")

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
    display_text("Item", item, "Added To Your Inventory")

def check_level_up():
    global level
    for lvl, xp_threshold in xp_levels.items():
        if xp >= xp_threshold:
            level = lvl

def shop():
    window_shop = tk.Toplevel(window)
    
    canvas_shop = tk.Canvas(window_shop, width = 400, height = 400)
    canvas_shop.pack()
    
    def shop_text(shp_txt):
         canvas_shop.create_text(200, 200, text = shp_txt, font = ("Arial", 16), fill = "black")

    shop_text("Shop Items And Prices:\n\n"
                 "Speed ~ $50\n"
                 "Strength ~ $50\n"
                 "Damage ~ $500\n"
                 "Attack Speed ~ $750\n"
                 "Movement Speed ~ $750\n"
                 "Flight ~ $1000")
    
    if can_fly:
        shop_text("Flight Speed ~ $500")
        
    shop_entry = tk.Entry(window_shop)
    shop_entry.pack()
    
    def shop_handle_input(event):
        game_info_value = shop_entry.get()
        if game_info_value == "1":
            window_shop.destroy()
            window.deiconify()
            window.focus_force()
            
    shop_entry.bind("<Return>", shop_handle_input)
    
def player_info():
    window_player_info = tk.Toplevel(window)
    
    canvas_player_info = tk.Canvas(window_player_info, width = 400, height = 400)
    canvas_player_info.pack()
    
    def player_info_text(plyr_info_txt):
         canvas_player_info.create_text(200, 200, text = plyr_info_txt, font = ("Arial", 16), fill = "black")
    
    global player_inventory
    
    player_info_text("Player Stats\n"
                 "____________\n\n"
                 "Player Health: " + str(player_health) + "\n"
                 "Attack Speed: " + str(attack_speed) + "\n"
                 "Inventory Slots: " + str(inventory_slots) + "\n"
                 "Money: " + str(money) + "\n"
                 "Current Level: " + str(level))
    
    if can_fly:
        player_info_text("Flight Speed: ", flight_speed)
      
    player_info_text("Player Inventory: " + ",".join(filtered_inventory))
        
    player_info_entry = tk.Entry(window_player_info)
    player_info_entry.pack()
    
    def handle_input(event):
        input_value = player_info_entry.get()
        if input_value == "1":
            window_player_info.destroy()
            window.deiconify()
            window.focus_force()
            
            
    player_info_entry.bind("<Return>", handle_input)
    
def credits():
    window_credits = tk.Toplevel(window)
    
    canvas_credits = tk.Canvas(window_credits, width = 400, height = 400)
    canvas_credits.pack()
    
    def credits_text(credits_txt):
         canvas_credits.create_text(200, 200, text = credits_txt, font = ("Arial", 16), fill = "black")
    
    credits_text("Developer: StinkyBagel")
    
    credits_entry = tk.Entry(window_credits)
    credits_entry.pack()
    
    def credit_handle_input(event):
        credit_input_value = credits_entry.get()
        if credit_input_value == "1":
            window_credits.destroy()
            window.deiconify()
            window.focus_force()
    
    credits_entry.bind("<Return>", credit_handle_input)        
            
def game_info():
    window_game_info = tk.Toplevel(window)
    
    canvas_game_info = tk.Canvas(window_game_info, width = 400, height = 400)
    canvas_game_info.pack()
    
    def game_info_text(game_info_txt):
         canvas_game_info.create_text(200, 200, text = game_info_txt, font = ("Arial", 16), fill = "black")
    
    game_info_text("The premise of the game is to fight enemies and gain xp and money."
                 "You can use the money to buy upgrades in the shop.")
    
    game_info_entry = tk.Entry(window_game_info)
    game_info_entry.pack()
    
    def game_info_handle_input(event):
        game_info_value = game_info_entry.get()
        if game_info_value == "1":
            window_game_info.destroy()
            window.deiconify()
            window.focus_force()
            
    game_info_entry.bind("<Return>", game_info_handle_input)

def main_menu():
    # global allows to be accessed and modified from different functions
    global player_health
    global attack_speed
    global inventory_slots
    global money
    global xp
    global found_items
    
    def main_menu_handle_input(event):
        title_options = main_menu_entry.get()
        if title_options == "1":
            window.withdraw()
            shop()
        elif title_options == "2":
            window.withdraw()
            player_info()
        elif title_options == "3":
            window.withdraw()
            credits()
        elif title_options == "4":
            window.withdraw()
            game_info()
    
    title_label = tk.Label(window, text = ("   _____ _                          _               _____ _           _     \n"
 "  / ____| |                        | |             / ____| |         | |    \n"
 " | |    | |__   __ _ _ __ __ _  ___| |_ ___ _ __  | |    | | __ _ ___| |__  \n"
 " | |    | '_ \ / _` | '__/ _` |/ __| __/ _ \ '__| | |    | |/ _` / __| '_ \ \n"
 " | |____| | | | (_| | | | (_| | (__| ||  __/ |    | |____| | (_| \__ \ | | |\n"
 "  \_____|_| |_|\__,_|_|  \__,_|\___|\__\___|_|     \_____|_|\__,_|___/_| |_|"))
    title_label.place(relx=0.5, rely=0.3, anchor="center")

    main_menu_label = tk.Label(window, text = "1.) Shop, 2.) Player Info, 3.) Credits, 4.) Game Info")
    main_menu_label.place(relx=0.5, rely=0.5, anchor="center")

    main_menu_entry = tk.Entry(window)
    main_menu_entry.place(relx=0.5, rely=0.6, anchor="center")
    
            
    main_menu_entry.bind("<Return>", main_menu_handle_input)
    
    
main_menu()

window.mainloop()