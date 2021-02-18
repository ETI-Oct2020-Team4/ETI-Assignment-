import townMenu
import globalVar
import pytest



globalVar.test_mode = True #Always put it there as true 

# Run Function
def test_run():
    
    globalVar.player.coordinate = 2
    globalVar.day = 1
    
    globalVar.combat_choice = "2" #set input for Menu input
    townMenu.combat_menu()
    
    globalVar.move_choice = "A"

    townMenu.move() # call menu function
    
    
    assert globalVar.player.coordinate == 1

    

def test_run_2():  
    
    globalVar.player.hp = 12
    globalVar.player.coordinate = 2
    globalVar.day = 1
    
    globalVar.combat_choice = "2" #set input for Menu input
    townMenu.combat_menu()
    
    globalVar.move_choice = "D"

    townMenu.move() # call menu function

    globalVar.combat_choice = "3"
    value = townMenu.combat_menu()
    
    
    assert globalVar.player.coordinate == 3
    assert value == "Please enter a valid option"

    
    

def test_run_3():
    
    globalVar.rat.hp = 8

    globalVar.player.coordinate = 2
    globalVar.day = 1
    
    globalVar.combat_choice = "2" #set input for Menu input
    townMenu.combat_menu()
    
    globalVar.move_choice = "D"

    townMenu.move() # call menu function

    assert globalVar.rat.hp == 10


   


