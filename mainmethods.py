import os
import keyboard
import pyfiglet
import calc

def main_SCREEN():
    clear_CONSOLE()
    astro = pyfiglet.figlet_format("ASTRO", font = "starwars", justify = "center")
    print(astro + "\n\n\n")
    print("Press enter to continue...\n")
    keyboard.read_key(suppress = True)

def clear_CONSOLE():
    os.system("cls" if os.name == "nt" else "clear")

def use_CHOICE(choice):
    match choice:
        case 1:
            height = calc.height_FROMSPEED()
            print("\nThe height of your satellite in orbit is approximately " + height + " kilometers.")
            print("\nPress enter to continue...")
            input()
        
        case 2:
            speed = calc.speed_FROMHEIGHT()
            print("\nThe speed of your satellite in orbit is approximately "+ speed + " meters per second.")
            print("\nPress enter to continue...")
            input()
        
        case 3:
            period = calc.period_ORBIT()
            print("\nThe period of your satellite in orbit is approximately: " + period + " hours.")
            print("\nPress enter to continue...")
            input()

        case _:
            print("\nNot a valid choice. Press enter to try again....")
            input()