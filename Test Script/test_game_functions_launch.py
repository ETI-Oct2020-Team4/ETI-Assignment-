import pytest
from .github/workflows.zzzzzzzzzz import *

@pytest.mark.parametrize("test_input,expected", [(3,"option 3")(4,"option 3")
                                                 (5,"option 3")(6,"option 3")
                                                 (7,"Please input a value from 1-5")
                                                 (8,"Error 0 < input <= 6")
                                                 (9,"Error 0 < input <= 6")
                                                 (0,"Error 0 < input <= 6")
                                                 (A,"Error 0 < input <= 6")])

def test_move():
    value = Town_Menu_Options(3)
    assert value == "option 3"

def test_rest():
    value = Town_Menu_Options(4)
    assert value == "option 4"

def test_save_game():
    value = Town_Menu_Options(5)
    assert value == "option 5" 

def test_exit_game():
    value = Town_Menu_Options(6)
    assert value == null

def test_wrong_input():
    value != Town_Menu_Options(7 or 8 or 9 or 0 or A)
    assert value == "Error 0 < input <= 6"




'''
def Town_Menu(input){
    if(input > 0 && < 10)
    return true

    }

'''
