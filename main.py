
print("Hello, Welcome to the clothing ordering chatbot.")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print("Hello " + name + ".")

def display_Options():
    print("\n Your Options:")
    print("1. Display menu")
    print("2. Browse Items")
    print("3. Check out cart")
    print("4. Exit program")
    


def user_Selection():
    in_use = True # True= program is running and False = program end
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 1:  #Go to Store Inventory.
       display_Options()
    elif user_choice == 2:  
        print("Browse items") 
    elif user_choice == 3:  
        print("checkout cart") 
    elif user_choice == 4:  #Exit the program
        in_use = False
        print("Goodbye, come back if you ever want to!")
    else:
       print("\nSorry, Not a Valid Choice. Please try again!")
       return in_use    

display_Options()
user_Selection()