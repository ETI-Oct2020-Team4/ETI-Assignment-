import townMenu
import globalVar
import pytest

globalVar.test_mode = True #Always put it there as true


def test_display_outdoor_menu():
    globalVar.player.coordinate = 2

    menu_options = ["1) View Character (Default)", "2) View Map", "3) Move", "4) Exit Game"]
    for choice in range(1, len(menu_options) + 1):
        globalVar.menu_choice = str(choice)
        
        assert townMenu.menu() == menu_options[choice - 1]
    
def test_outdoor_menu_1():
    globalVar.menu_choice = "1" #set input

    value = townMenu.menu() #call the menu 

    assert value == "1"

def test_outdoor_menu_2():
    globalVar.menu_choice = "2" #set input

    value = townMenu.menu() #call the menu 

    assert value == "2"

def test_outdoor_menu_3():
    globalVar.menu_choice = "3" #set input

    value = townMenu.menu() #call the menu 

    assert value == "3"

def test_outdoor_menu_4():
    checklist = []
    tudtestbase.set_keyboard_input([""]) #this is requiredd regardless of input 


    globalVar.menu_choice = "4" #set input
     
    
    value = townMenu.menu() #call the menu 
    tudtestbase.get_display_output() #get all printed values

    for i in tudtestbase.print_values: #a list called print_values that store all prints
        if i == "EXIT": #check for print game exited
            checklist.append(i)
    
    assert checklist == ["EXIT"]

    
    
