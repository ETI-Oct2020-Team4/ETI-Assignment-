import pytest
import main
import globalVar
import townMenu

globalVar.test_mode = True #prevents menu function from looping

def test_resume_game():
   
    globalVar.player.hp = 10

    globalVar.player.has_orb = True

    globalVar.player.defence = 0

    globalVar.player.coordinate = 1

    globalVar.menu_choice = "4"

    townMenu.menu()

    globalVar.menu_choice = "2"

    main.menu()

    assert globalVar.player.hp == 10

    assert globalVar.player.has_orb == True

    assert globalVar.player.defence == 0

    assert globalVar.player.coordinate == 1
    
