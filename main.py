
print("Hello, Welcome to the clothing ordering chatbot.")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print("Hello " + name + "feel free to use the return bot.")

def display_Options():
    print("\n Your Options:")
    print("1. Display menu")
    print("2. return items")
    print("3. Exit program")
    
def return_items():
    returned_items = []  
    print("Please enter the names of items you'd like to return. Type 'done' when finished.")
    
    while True:
        item = input("Enter item name: ")
        if item.lower() == 'done':  
            break
        else:
            returned_items.append(item)  
            print(f"{item} has been added to your return list.")
    
    if returned_items:
        print("\nYou have returned the following items:")
        for item in returned_items:
            print(f"- {item}")
    else:
        print("You did not return any items.")

def user_Selection():
    in_use = True 
    user_choice = int(input("Enter a number between 1-3: "))
    if user_choice == 1:  
       display_Options()
    elif user_choice == 2:  
        return_items()
    elif user_choice == 3:  
       in_use = False
       print("Goodbye, come back if you ever want to!")
    else:
       print("\nSorry, Not a Valid Choice. Please try again!")
       return in_use    

display_Options()

user_Selection()