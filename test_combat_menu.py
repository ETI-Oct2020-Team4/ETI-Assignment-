import globalVar
import pytest
import player
import tudtestbase
import townMenu

globalVar.test_mode = True #do not change
        
# Combat Menu (method 2)
def test_combat_menu_1():
 # when player inputs option '1'
    globalVar.menu_choice = "1" #set input

    value = townMenu.combat_menu()  #call the menu

    assert value == "1"

def test_combat_menu_2():
 # when player inputs option '2'
    globalVar.menu_choice = "2" #set input

    value = townMenu.combat_menu() #call the menu

    assert value == "2"

def test_wrong_input_1():
 # when player presses Enter button
    globalVar.menu_choice = ""

    value = townMenu.combat_menu() #call the menu

    assert value == "error"

def test_wrong_input_2():
 # when player inputs option '3' or more
    globalVar.menu_choice = "3"

    value = townMenu.combat_menu() #call the menu

    assert value == "error"

def test_wrong_input_3():
 # when player inputs symbol '$' or others
    globalVar.menu_choice = "$"

    value = townMenu.combat_menu() #call the menu

    assert value == "error"

def test_wrong_input_4():
 # when player inputs letter 'A' or others. Can be either uppercase or lowercase.
    globalVar.menu_choice = "A"

    value = townMenu.combat_menu() #call the menu 

    assert value == "error"
