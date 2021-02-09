import random
import globalVar
import player

def menu():
    #print text and menu 
    print("\nDay " + str(globalVar.day) + ": You are in a town.") 
   
    menu_options = ["1) View Character", "2) View Map", "3) Move","4) Rest", "5) Save", "6) Exit"]
   
    for option in menu_options:
        print(option)

    #ask for input
    if globalVar.test_mode:
        menu_choice = globalVar.menu_choice
    else:
        menu_choice = input("Enter choice: ")


    #check option choice with input 
    if menu_choice == "1":
        if not globalVar.test_mode: #loop menu if test mode not on
            menu()
        return "1"
    elif menu_choice == "2":
        if not globalVar.test_mode:
            menu()
        return "2"
    elif menu_choice == "3":
        return "3"
      
    elif menu_choice == "4":
        if not globalVar.test_mode:
            menu()
        return "4"
    
    elif menu_choice == "5":
        if not globalVar.test_mode:
            menu()
        return "5"
    
    elif menu_choice == "6":
        print("Game Exited")
        if globalVar.test_mode == False:
            exit()
        
    else:
        print("Error: Invalid Input") #check invalid input
        if not globalVar.test_mode:
            menu()
        return "error"
    
    try:
        selected_option = menu_options[int(menu_choice) - 1]
        return selected_option
    except IndexError:
        return menu_options[0]

    
