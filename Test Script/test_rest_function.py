import townMenu
import globalVar
import pytest

globalVar.test_mode = True #Always put it there as true 

# Rest Function
def test_rest_2():  #done
    globalVar.player.hp = 12 #set current hero hp 

    globalVar.menu_choice = "4" #set input for Menu input

    townMenu.menu() # call menu function

    assert globalVar.player.hp == 20
    

def test_rest_3(): #need sara to code
    globalVar.player.hp = 20 #set current hero hp 

    checklist = []
    tudtestbase.set_keyboard_input([""]) #this is requiredd regardless of input 


    globalVar.menu_choice = "4" #set input
     
    
    value = townMenu.menu() #call the menu 
    tudtestbase.get_display_output() #get all printed values

    for i in tudtestbase.print_values: #a list called print_values that store all prints
        if i == "Error: Hero is unable to Rest": #check for print game exited
            checklist.append(i)
    
    assert checklist == ["Error: Hero is unable to Rest"]
    

def test_rest_4(): #done
    globalVar.day = 2 #set current day

    globalVar.menu_choice = "4" #set input for Menu input

    townMenu.menu() # call menu function

    assert globalVar.day == 3

