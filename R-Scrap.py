import requests
from bs4 import BeautifulSoup
import os

# Colors for text
PURPLE = '\033[95m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Facebook Cookie (User can either input cookie or username/password)
cookie = ""
username = ""
password = ""

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
    """ + "-" * 50 + RESET)

# Get Facebook login credentials
def get_credentials():
    global cookie, username, password

    # Prompt for cookie or login details
    choice = input("Login with (1) Cookie or (2) Username/Password: ").strip()

    if choice == '1':
        cookie = input("Enter your Facebook cookie: ")
        print("Cookie set successfully!")
    elif choice == '2':
        username = input("Enter your Facebook username: ")
        password = input("Enter your Facebook password: ")
        print("Login details set successfully!")
    else:
        print("Invalid choice. Please enter a valid option.")
        get_credentials()

# Function to fetch friends list from Facebook
def fetch_friends_list(url, cookies):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    
    # Check if we have cookie or login details
    cookies = {
        "datr": cookie.split(";")[0].split("=")[1],
        "sb": cookie.split(";")[1].split("=")[1],  # Add more cookies as necessary
    }

    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        friends = []
        for friend in soup.find_all('a', {'class': 'friend'}):  # Adjust class name as needed
            friend_id = friend.get('href').split('=')[-1]
            friends.append(friend_id)
        return friends
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return []

# Function to prompt for directory and save results
def save_scraped_data(friends):
    directory = input("Enter the directory to save the scraped data (e.g., /sdcard/test.txt): ").strip()
    filename = os.path.join(directory, "test.txt")

    with open(filename, 'w') as file:
        for friend in friends:
            file.write(f"{friend}\n")
    print(f"Scraped data saved to {filename}")

# Main script logic
def main():
    os.system('clear')
    display_logo()
    display_menu()

    # Get login credentials (either cookie or username/password)
    get_credentials()

    choice = input("Choose option: ").strip()

    if choice == '1':
        print("Fetching friends for a single ID...")
        friends = fetch_friends_list("https://m.facebook.com/100085597518314/friends", cookies)
        if friends:
            print(f"Found {len(friends)} friends.")
            save_scraped_data(friends)
        else:
            print("No friends found or failed to fetch data.")
    elif choice == '2':
        print("Fetching friends for unlimited IDs...")
        # Multiple user IDs as example
        user_ids = ["100085597518314", "100084884637391"]
        for user_id in user_ids:
            print(f"Fetching friends for {user_id}...")
            friends = fetch_friends_list(f"https://m.facebook.com/{user_id}/friends", cookies)
            if friends:
                print(f"Found {len(friends)} friends for {user_id}.")
                save_scraped_data(friends)
            else:
                print(f"Failed to retrieve friends for {user_id}.")
    elif choice == '3':
        print("Exiting program...")
    elif choice == '0':
        print("Cookie removed!")
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
