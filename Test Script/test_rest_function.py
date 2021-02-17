import townMenu
import globalVar
import pytest


globalVar.test_mode = True #Always put it there as true 

# Rest Function
def test_rest_2():  #done
    globalVar.player.hp = 12 #set current hero hp 

    townMenu.rest() # call menu function

    assert globalVar.player.hp == 20
    

def test_rest_3(): 
    globalVar.player.hp = 20 #set current hero hp 
   
    value = townMenu.rest() #call the menu
    assert value == "Error: Hero is unable to Rest"
    

def test_rest_4(): #done
    globalVar.day = 2 #set current day
    globalVar.player.hp = 12

    townMenu.rest() # call menu function

    assert globalVar.day == 3

