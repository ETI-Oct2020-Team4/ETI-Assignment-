import townMenu
import globalVar
import pytest

globalVar.test_mode = True #Always put it there as true


def test_save_function():
    globalVar.day = 3
    globalVar.player.damage = "2-4"
    globalVar.player.defence = 2
    globalVar.player.hp = 15
    globalVar.player.coordinate = 12
    globalVar.player.has_orb = True
    
    
    
    globalVar.menu_choice = "5" #set input for Menu input

    townMenu.menu() # call menu function

    f = open("gamesave.txt", "r")
    save_data = f.read()
    save_data_components = save_data.split(",")


    assert int(save_data_components[0]) == 3
    assert save_data_components[1] == "The Hero"
    assert save_data_components[2] == "2-4"
    assert int(save_data_components[3]) == 2
    assert int(save_data_components[4]) == 15
    assert int(save_data_components[5]) == 12
    assert eval(save_data_components[6]) == True
    

    
    
