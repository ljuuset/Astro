import pyfiglet
import keyboard
import math
import time
import os

def clear_CONSOLE():
    os.system("cls" if os.name == "nt" else "clear")

def use_CHOICE(choice):
    match choice:
        case 1:
            height = height_FROMSPEED()
            print("\nThe height of your satellite in orbit is approximately " + height + " kilometers.")
            print("\nPress enter to continue...")
            input()
            
        case 2:
            speed = speed_FROMHEIGHT()
            print("\nThe speed of your satellite in orbit is approximately "+ speed + " meters per second.")
            print("\nPress enter to continue...")
            input()
            
        case _:
            print("\nNot a valid choice. Press enter to try again....")
            input()

def height_FROMSPEED():
    mass_ONE = float(input("Mass of the central body in kg (scientific notation): "))
    radius_ONE = float(input("Radius of the central body in meters (scientific notation): "))
    speed_TWO = float(input("Speed of the satellite body in meters per second: "))
    
    radius = (big_G*mass_ONE)/(speed_TWO**2)
    height = round((radius-radius_ONE)/1000, 4)
    
    return str(height)

def speed_FROMHEIGHT():
    mass_ONE = float(input("Mass of the central body in kg (scientific notation): "))
    radius_ONE = float(input("Radius of the central body in meters (scientific notation): "))
    height_TWO = float(input("Orbital height of the satellite body in meters (scientific notation): "))
    
    speed = round(math.sqrt((big_G*mass_ONE)/(radius_ONE+height_TWO)), 4)
    return str(speed)

p = 1
big_G = float(6.67428e-11)

clear_CONSOLE()
astro = pyfiglet.figlet_format("ASTRO", font = "starwars", justify = "center")
print(astro + "\n\n\n")
print("Press enter to continue...\n")
keyboard.read_key(suppress = True)

while(p == 1):
    clear_CONSOLE()
    print("Select a function\n1. Orbit height from speed\n2. Orbit speed from height\n0. Quit\n\n")
    function_Choice = int(input("Choice: "))
    time.sleep(1)
    clear_CONSOLE()
    
    if function_Choice == 0:
        p = 0
    
    else:
        use_CHOICE(function_Choice)