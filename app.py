# Importing JSON file that's used to save and load grocery list from a file
import json
# File used to store the grocery list permanently 
DATA_FILE = "data.json"
# This is used to load existing items from the file
def load_items():
    # Opening file in read mode
    try:
        with open(DATA_FILE, "r") as file:
            # Converting JSON data into a Python list and return it
            return json.load(file)
    except:
        return []
    
# This is used to save the list into the JSON file
def save_items(items):
    # Opening the file in write mode so it can overwrite and change the data
    with open(DATA_FILE, "w") as file:
        # Convert Python list into JSON format and store it
        json.dump(items, file)

# This function displays all the items in a clean list
def show_items(items):
    # If list is empty, show message and stop
    if not items:
        print("No groceries yet...")
        return
    # Printing the title
    print("\nGrocery List:")
    # Loop through items with numbers starting at 1
    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")
    
# For adding items to the list
def add_item(items):
    # Asking for the user's input 
    item = input("Enter item to add: ")
    # Add item to list
    items.append(item)
    # Confirm action
    print(f"Added: {item}")

# This function removes an item from the list
def remove_item(items):
        # Show the current list
        show_items(items)
        try:
            # Ask user which number to remove
            index = int(input("Enter number to remove:")) - 1
            # Remove item at that position
            removed = items.pop(index)
            # Confirm removal
            print(f"Removed: {removed}")
        except:
            # If user enters invalid input
            print("Invalid choice")
        
# Main program loop 
def main():
    # Load existing grocery list from file
    items = load_items()
    # Infinite loop so menu will keep showing
    while True:
        print("\n--- Grocery App ---")
        print("1. View items")
        print("2. Add item")
        print("3. Remove item")
        print("4. Exit")
        # Getting user choice
        choice = input("Choose: ").strip()
        # Decide what to do based on what the user inputs
        if choice == "1":
            show_items(items)

        elif choice == "2":
            add_item(items)
            save_items(items)

        elif choice == "3":
            remove_item(items)
            save_items(items)

        elif choice == "4":
            # Save before exiting
            save_items(items)
            break

        else:
            print("Invalid option")

# Starting the program here
main()