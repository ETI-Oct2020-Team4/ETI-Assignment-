import townMenu
import globalVar
import pytest

globalVar.test_mode = True #Always put it there as true


def test_outdoor_menu_1():
    globalVar.rat.hp = 0
    
    value = townMenu.combat_menu()
    assert value == "The rat has been defeated."

    
def test_outdoor_menu_2():
    globalVar.player.coordinate = 2

    menu_options = ["1", "2", "3", "4"]
    for choice in range(1, len(menu_options) + 1):
        globalVar.menu_choice = str(choice)
        
    assert townMenu.menu() == menu_options[choice - 1]
    
    
def test_outdoor_menu_3():
    globalVar.menu_choice = "1" #set input

    value = townMenu.menu() #call the menu 

    assert value == "1"

def test_outdoor_menu_4():
    globalVar.menu_choice = "2" #set input

    value = townMenu.menu() #call the menu 

    assert value == "2"

def test_outdoor_menu_5():
    globalVar.menu_choice = "3" #set input

    value = townMenu.menu() #call the menu 

    assert value == "3"


    
    
