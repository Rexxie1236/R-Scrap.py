import requests
from bs4 import BeautifulSoup
import os

# Colors for text
PURPLE = '\033[95m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Facebook Cookie (User can input their cookie)
cookie = ""

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
def get_cookie():
    global cookie
    cookie = input("Enter your Facebook cookie: ").strip()
    if not cookie:
        print("No cookie provided. You cannot proceed without a cookie.")
        exit()

# Fetch friends list for a given Facebook ID
def fetch_friends_list(user_id):
    url = f"https://m.facebook.com/{user_id}/friends"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie": cookie,
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print(f"Successfully fetched data for user ID: {user_id}")
        soup = BeautifulSoup(response.text, 'html.parser')
        friends = []
        for friend in soup.find_all('a', href=True):
            if "friends/hovercard" in friend['href']:
                friends.append(friend.text)
        return friends
    else:
        print(f"Failed to retrieve page for user ID {user_id}. Status code: {response.status_code}")
        return []

# Save friends list to the specified directory
def save_to_file(friends):
    directory = input("Enter the directory to save the scraped data (e.g., /sdcard/test.txt): ").strip()
    try:
        with open(directory, 'w') as file:
            for friend in friends:
                file.write(f"{friend}\n")
        print(f"Scraped data saved to {directory}")
    except Exception as e:
        print(f"Failed to save data. Error: {e}")

# Main script logic
def main():
    os.system('clear')
    display_logo()
    display_menu()

    # Ensure login via cookie
    if not cookie:
        get_cookie()

    choice = input("Choose option: ").strip()

    if choice == '1':
        user_id = input("Enter the Facebook ID to scrape: ").strip()
        print(f"Fetching friends for user ID: {user_id}...")
        friends = fetch_friends_list(user_id)
        if friends:
            print(f"Found {len(friends)} friends.")
            save_to_file(friends)
        else:
            print("No friends found or failed to fetch data.")
    elif choice == '2':
        print("Fetching friends for multiple IDs...")
        user_ids = input("Enter Facebook IDs separated by commas: ").strip().split(',')
        all_friends = []
        for user_id in user_ids:
            print(f"Fetching friends for {user_id}...")
            friends = fetch_friends_list(user_id)
            all_friends.extend(friends)
        if all_friends:
            print(f"Found {len(all_friends)} total friends.")
            save_to_file(all_friends)
        else:
            print("No friends found or failed to fetch data.")
    elif choice == '3':
        print("Exiting program...")
    elif choice == '0':
        global cookie
        cookie = ""
        print("Cookie removed!")
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
