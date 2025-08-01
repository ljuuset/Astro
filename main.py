import time
import mainmethods

def main():
    while True:
        mainmethods.clear_CONSOLE()
        print("Select a function\n1. Orbit height from speed\n2. Orbit speed from height\n3. Period of orbit"
              "\n0. Quit\n\n")
        function_Choice = int(input("Choice: "))
        time.sleep(1)
        mainmethods.clear_CONSOLE()
    
        if function_Choice == 0:
            break
        else:
            mainmethods.use_CHOICE(function_Choice)

mainmethods.main_SCREEN()

if __name__ == "__main__":
    main()