import requests
from bs4 import BeautifulSoup
import os

# Colors for text
PURPLE = '\033[95m'
GREEN = '\033[92m'
RESET = '\033[0m'

# Facebook Login Cookie (ensure this is up to date)
cookie = input("Enter cookie: ")

# Facebook URL (target page, e.g., profile, friends list)
url = "https://m.facebook.com/100085597518314/friends"  # Example profile

# Set up headers and cookies for the requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}
cookies = {
    "datr": cookie.split(";")[0].split("=")[1],  # Replace with actual cookie string
    "sb": cookie.split(";")[1].split("=")[1],    # Example cookie extraction
    # Add other cookie pairs here as needed
}

def fetch_friends_list(url, cookies):
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        friends = []
        # You will need to find the correct HTML elements that list the friends
        for friend in soup.find_all('a', {'class': 'friend'}):  # Adjust class name for friends
            friend_id = friend.get('href').split('=')[-1]  # Extract the friend ID
            friends.append(friend_id)
        return friends
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return []

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

def display_menu():
    print(GREEN + """
    1. Extract with single ID
    2. Extract with unlimited IDs
    3. Exit Program
    0. Remove Cookie
    """ + "-" * 50 + RESET)

def main():
    os.system('clear')
    display_logo()
    display_menu()

    choice = input("Choose option: ").strip()

    if choice == '1':
        print("Fetching friends for a single ID...")
        friends = fetch_friends_list(url, cookies)
        if friends:
            print(f"Found {len(friends)} friends.")
            for friend in friends:
                print(friend)
    elif choice == '2':
        print("Fetching friends for unlimited IDs...")
        # You would want to loop over multiple IDs here
        # For simplicity, this is just a placeholder example
        user_ids = ["100085597518314", "100084884637391"]
        for user_id in user_ids:
            print(f"Fetching friends for {user_id}...")
            friends = fetch_friends_list(f"https://m.facebook.com/{user_id}/friends", cookies)
            if friends:
                print(f"Found {len(friends)} friends for {user_id}.")
                for friend in friends:
                    print(friend)
    elif choice == '3':
        print("Exiting program...")
    elif choice == '0':
        print("Cookie removed!")
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
