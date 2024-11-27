import os

# Colors for text
PURPLE = '\033[95m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Display logo and welcome message
def display_logo():
    print(PURPLE + """
     ____  _______  ___  __ __________    __________  ____  ______
    / __ \/ ____/ |/ / |/ //  _/ ____/   / ____/ __ \/ __ \/ ____/
   / /_/ / __/  |   /|   / / // __/     / /   / / / / /_/ / __/
  / _, _/ /___ /   |/   |_/ // /___    / /___/ /_/ / _, _/ /___
 /_/ |_/_____//_/|_/_/|_/___/_____/____\____/\____/_/ |_/_____/
                                /_____/
     """ + RESET)
    ("-" * 50+ RESET)
    print(GREEN + "WELCOME TO REXXIE_WORLD")
    print("Author: REXXIE")
    print("Program Name: R-Scrap.py")
    print("Programmers ID: 08101217448")
    print("-" * 50 + RESET)

# Display menu
def display_menu():
    print(GREEN + """
    1. Extract with single ID
    2. Extract with unlimited IDs
    3. Exit Program
    0. Remove Cookie
    ("-" * 50 + RESET)

# Main script logic
def main():
    os.system('clear')
    display_logo()
    display_menu()

    choice = input("Choose option: ").strip()
    if choice == '1':
        print("Functionality for option 1 will go here.")
    elif choice == '2':
        print("Functionality for option 2 will go here.")
    elif choice == '3':
        print("Exiting program...")
    elif choice == '0':
        print("Cookie removed!")
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
