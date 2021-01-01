character_Stats = ["The Hero", "2-4" , "1" ,"20"]

def Show_Character_Stats():
    print(character_Stats[0]);
    print(" Damage: " + character_Stats[1]);
    print("Defense: " + character_Stats[2]);
    print("     HP: " + character_Stats[3]);
    toString = character_Stats[0] + character_Stats[1] + character_Stats[2] + character_Stats[3]
    print(toString)
    return toString 

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

    Town_Menu_Options(option);
        
    

def Town_Menu_Options(o_input):

    message = ""
    if (o_input == "1"):
        Show_Character_Stats();
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
    
