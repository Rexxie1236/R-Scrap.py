import os

# Display logo in purple
logo = """
\033[35m ____  _______  ___  __ __________    __________  ____  ______
   / __ \\/ ____/ |/ / |/ //  _/ ____/   / ____/ __ \\/ __ \\/ ____/
  / /_/ / __/  |   /|   / / // __/     / /   / / / / /_/ / __/
 / _, _/ /___ /   |/   |_/ // /___    / /___/ /_/ / _, _/ /___
/_/ |_/_____//_/|_/_/|_/___/_____/____\____/\____/_/ |_/_____/
                                /_____/

"""

# Welcome message
print(logo)
print("\033[32m----------------------------------------------")
print("\033[32mWELCOME TO REXXIE_WORLD")
print("\033[32mAuthor - REXXIE")
print("\033[32mProgram Name : R-Scrap.py")
print("\033[32mProgrammers ID : 08101217448")
print("\033[32m----------------------------------------------")

# Main menu options
while True:
    print("\033[32m1. Extract with single Id")
    print("2. Extract with unlimited Ids")
    print("3. Exit Program")
    print("0. Remove Cookie")
    print("\033[32m----------------------------------------------")
    
    # Get user input for option
    choice = input("\033[32mChoose option: ")

    if choice == '1':
        print("\033[34mFetching friends list for single ID...")
        # Add the functionality of fetching friends for a single ID here
    elif choice == '2':
        print("\033[34mFetching friends list for multiple IDs...")
        # Add the functionality of fetching friends for multiple IDs here
    elif choice == '3':
        print("\033[32mExiting program...")
        break
    elif choice == '0':
        print("\033[32mRemoving cookies...")
        # Add the cookie removal functionality here
    else:
        print("\033[31mInvalid option. Please choose again.")
