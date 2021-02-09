import townMenu
import globalVar
import pytest
import player
import tudtestbase

globalVar.test_mode = True #always be true

def test_display_town_menu_1():
    globalVar.menu_choice = "1" #set input

    value = townMenu.menu() #call the menu 

    assert value == "1"

def test_display_town_menu_2():
    globalVar.menu_choice = "2" #set input

    value = townMenu.menu() #call the menu 

    assert value == "2"

def test_display_town_menu_3():
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
    checklist = []
    tudtestbase.set_keyboard_input([""]) #this is requiredd regardless of input 


    globalVar.menu_choice = "6" #set input
     
    
    value = townMenu.menu() #call the menu 
    tudtestbase.get_display_output() #get all printed values

    for i in tudtestbase.print_values: #a list called print_values that store all prints
        if i == "Game Exited": #check for print game exited
            checklist.append(i)
    
    assert checklist == ["Game Exited"]

def test_wrong_input_1():
    globalVar.menu_choice = ""

    value = townMenu.menu() #call the menu 

    assert value == "error"

def test_wrong_input_2():
    globalVar.menu_choice = "7"

    value = townMenu.menu() #call the menu 

    assert value == "error"

def test_wrong_input_3():
    globalVar.menu_choice = "$"

    value = townMenu.menu() #call the menu 

    assert value == "error"

def test_wrong_input_4():
    globalVar.menu_choice = "A"

    value = townMenu.menu() #call the menu 

    assert value == "error"
    
    
