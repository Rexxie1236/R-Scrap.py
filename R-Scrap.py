import os

# Colors for text
PURPLE = '\033[95m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Path to store the cookie file
COOKIE_FILE = "cookie.txt"

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
    print(GREEN + "-" * 50)
    print("WELCOME TO REXXIE_WORLD")
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
    """ + "-" * 50 + RESET)

# Function to get or save a cookie
def get_cookie():
    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, "r") as file:
            return file.read().strip()
    else:
        print("Cookie file not found. Please provide a new cookie.")
        cookie = input("Enter cookie: ").strip()
        with open(COOKIE_FILE, "w") as file:
            file.write(cookie)
        return cookie

# Function to remove a cookie
def remove_cookie():
    if os.path.exists(COOKIE_FILE):
        os.remove(COOKIE_FILE)
        print("Cookie removed successfully!")
    else:
        print("No cookie found to remove.")

# Functionality for option 1
def extract_single_id(cookie):
    print(GREEN + "Enter the file path to save: " + RESET, end="")
    save_path = input().strip()
    print(GREEN + "Enter the Facebook user ID: " + RESET, end="")
    user_id = input().strip()
    print(f"Debug: Fetching friends list for user ID {user_id}...")
    with open(save_path, "w") as file:
        file.write(f"Mock data for user ID {user_id}\n")
    print(f"Data saved to {save_path}.")

# Functionality for option 2
def extract_multiple_ids(cookie):
    print(GREEN + "Enter the file path to save: " + RESET, end="")
    save_path = input().strip()
    print(GREEN + "How many user IDs would you like to add? " + RESET, end="")
    count = int(input().strip())
    user_ids = []
    for i in range(count):
        print(f"Enter Facebook user ID/Username {i+1}: ", end="")
        user_ids.append(input().strip())
    print(f"Debug: Fetching friends list for {count} user IDs...")
    with open(save_path, "w") as file:
        for idx, user_id in enumerate(user_ids, 1):
            file.write(f"{idx} - {user_id}|Mock Name\n")
    print(f"Data saved to {save_path}.")

# Main script logic
def main():
    os.system('clear')
    display_logo()

    cookie = get_cookie()
    while True:
        display_menu()
        choice = input("Choose option: ").strip()
        if choice == '1':
            extract_single_id(cookie)
        elif choice == '2':
            extract_multiple_ids(cookie)
        elif choice == '3':
            print("Exiting program...")
            break
        elif choice == '0':
            remove_cookie()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
