import townMenu
import globalVar
import pytest

globalVar.test_mode = True #Always put it there as true 

# Rat Appear Function
def test_rat_appear_1():
    
    globalVar.player.coordinate = 2
    globalVar.player.hp = 10
    globalVar.rat.damage = "2-2"
    
    townMenu.combat_menu()
     
    assert globalVar.player.hp == 9
    

def test_rat_appear_2():  
    
    globalVar.player.coordinate = 2
    globalVar.player.hp = 10
    globalVar.rat.damage = "2-2"
    
    globalVar.move_choice = "A"

    townMenu.move()
     
    assert globalVar.player.hp == 10
