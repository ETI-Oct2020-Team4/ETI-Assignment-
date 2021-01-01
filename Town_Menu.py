def Town_Menu():
    #print out menu
    print("You are in a town.");
    print("1) View Character");
    print("2) View Map");
    print("3) Move");
    print("4) Rest");
    print("5) Save Game");
    print("6) Exit Game");
    #ask for input
    option = input("Please enter an Option: "); 

    Town_Menu_Options(option);
        
    

def Town_Menu_Options(o_input):

    message = ""
    if (o_input == "1"):

        message = "option 1";
        
    elif (o_input == "2"):
        
        message = "option 2";
        
    elif (o_input == "3"):
        
        message = "option 3";
        
    elif (o_input == "4"):
        
        message = "option 4";
        
    elif (o_input == "5"):
        
        message = "option 5";
        

    elif (o_input == "6"):
        message = "option 6"
         
    else:
        message = "Error";

    print(message + "\n");
    return message;


while(True):
    Town_Menu() 
    
