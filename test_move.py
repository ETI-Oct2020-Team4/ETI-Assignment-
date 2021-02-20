import townMenu
import globalVar
import pytest
<<<<<<< Updated upstream
import player
import tudtestbase
=======
>>>>>>> Stashed changes

globalVar.test_mode = True #always be true

def test_move_1():
<<<<<<< Updated upstream
    globalVar
=======
    globalVar.player.coordinate = 9
     
    globalVar.move_choice = "W" #set input
    townMenu.move()
    
    assert globalVar.player.coordinate == 1

def test_move_2():
    globalVar.player.coordinate = 2
    
    globalVar.move_choice = "A" #set input
    townMenu.move()
    
    assert globalVar.player.coordinate == 1

def test_move_3():
    globalVar.player.coordinate = 1
    
    globalVar.move_choice = "S" #set input
    townMenu.move()
    
    assert globalVar.player.coordinate == 9

def test_move_4():
    globalVar.player.coordinate = 1
    
    globalVar.move_choice = "D" #set input
    townMenu.move()
    
    assert globalVar.player.coordinate == 2


#Test Map Top Edge
def test_map_top_edge():
    globalVar.player.coordinate = 1

    globalVar.move_choice = "W" #set input 
    townMenu.move()

    assert globalVar.player.coordinate == 1


    #Test Map Bottom Edge
def test_map_bottom_edge():
    globalVar.player.coordinate = 64

    globalVar.move_choice = "S" #set input    
    townMenu.move()

    assert globalVar.player.coordinate == 64

#Test Map Right Edge
def test_map_right_edge():
    globalVar.player.coordinate = 16

    globalVar.move_choice = "D" #set input
    townMenu.move()

    assert globalVar.player.coordinate == 16  

#Test Map Left Edge
def test_map_left_edge():
    globalVar.player.coordinate = 9

    globalVar.move_choice = "A" #set input
    townMenu.move()

    assert globalVar.player.coordinate == 9

#Test Invalid Input
def test_wrong_input_5():
    globalVar.move_choice = "$5Z" #set input

    value = townMenu.move()
    assert value == "Invalid Input"

#Test Day + 1
def test_day_move():

    globalVar.move_choice = "D" #set input
    globalVar.day = 1
    townMenu.move()
    
    assert globalVar.day == 2


>>>>>>> Stashed changes
