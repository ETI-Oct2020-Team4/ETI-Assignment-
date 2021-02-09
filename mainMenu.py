import globalVar


def menu():
    #print out menu
    print("\nWelcome to Ratventure!\n----------------------")
    print("1) New Game")
    print("2) Resume Game")
    print("3) Exit Game")

    #check for test mode
    if globalVar.test_mode:
        menu_choice = globalVar.menu_choice
    else:
        menu_choice = input("Enter choice: ")

    #check for input choice

    if menu_choice == "1":
        return "1"
    
    elif menu_choice == "2":
        return "2"
        
    elif menu_choice == "3":
        return "3"
     
    else:  #check for invalid input 
        print("Error: Invalid Input")
        if globalVar.test_mode == False:
            menu()
        return "error"
