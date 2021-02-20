import townMenu
import globalVar
import pytest

globalVar.test_mode = True #always be true

def test_view_character_1():
    globalVar.menu_choice = "1" #set input

    value = townMenu.menu() #call the menu 

    assert value == "1"

def test_view_map_1():
    globalVar.menu_choice = "2" #set input

    value = townMenu.menu() #call the menu 

    assert value == "2"

def test_move_1():
    globalVar.menu_choice = "3" #set input

    value = townMenu.menu() #call the menu 

    assert value == "3"

def test_display_town_menu_4():
    globalVar.menu_choice = "4" #set input

    value = townMenu.menu() #call the menu 

    assert value == "4"

def test_display_town_menu_5():
    globalVar.menu_choice = "5" #set input

    value = townMenu.menu() #call the menu 

    assert value == "5"

def test_display_town_menu_6():
    
    globalVar.menu_choice = "6" #set input

    value = townMenu.menu() #call the menu 

    assert value == "6"

def test_wrong_input_1():
    globalVar.menu_choice = ""

    value = townMenu.menu() #call the menu 

    assert value == "Please enter a valid option"

def test_wrong_input_2():
    globalVar.menu_choice = "7"

    value = townMenu.menu() #call the menu 

    assert value == "Please enter a valid option"

def test_wrong_input_3():
    globalVar.menu_choice = "$"

    value = townMenu.menu() #call the menu 

    assert value == "Please enter a valid option"

def test_wrong_input_4():
    globalVar.menu_choice = "A"

    value = townMenu.menu() #call the menu 

    assert value == "Please enter a valid option"
    
    
