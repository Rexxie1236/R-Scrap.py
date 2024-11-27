import os


---

### **Updating Your Code to Match This Flow**
Your current code likely repeats the welcome message whenever the menu reappears. To fix this, you can structure your program to display the welcome message only once when the program starts. Here's a sample structure in Python:

```python
logo = r"""
____  _______  ___  __ __________    __________  ____  ______
/ __ \/ ____/ |/ / |/ //  _/ ____/   / ____/ __ \/ __ \/ ____/
/ /_/ / __/  |   /|   / / // __/     / /   / / / / /_/ / __/
/ _, _/ /___ /   |/   |_/ // /___    / /___/ /_/ / _, _/ /___
/_/ |_/_____//_/|_/_/|_/___/_____/____\____/\____/_/ |_/_____/
                             /_____/"""

welcome_message = """
----------------------------------------------
WELCOME TO REXXIE_WORLD
Author - REXXIE
Program Name : R-Scrap.py
Programmers ID : 08101217448
----------------------------------------------
"""
menu = """
----------------------------------------------
1. Extract with single Id
2. Extract with unlimited Ids
3. Exit Program
0. Remove Cookie
----------------------------------------------
Choose option:
"""

# Display the logo and welcome message only once
print(logo)
print(welcome_message)

# Main program loop
while True:
 print(menu)
 choice = input("> ").strip()
 
 if choice == "1":
     print("You selected option 1: Extract with single Id")
     # Add functionality for option 1 here
 elif choice == "2":
     print("You selected option 2: Extract with unlimited Ids")
     # Add functionality for option 2 here
 elif choice == "3":
     print("Exiting the program. Goodbye!")
     break
 elif choice == "0":
     print("Removing cookies...")
     # Add functionality to remove cookies here
 else:
     print("Invalid option. Please try again.")
