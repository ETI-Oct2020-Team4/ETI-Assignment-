import pytest
from Town_Menu import *


@pytest.mark.parametrize("test_input,expected", [(1,"option 1"),(2,"option 2"),(3,"option 3"),
                                                 (4,"option 4"),(5,"option 5"),
                                                 (6,"option 6"),(7,"Error"),(8,"Error"),

                                                 (9,"Error"),(0,"Error"),("A","Error")])

def test_wrong_input(test_input,expected):
      value = Town_Menu(test_input)
      assert value == expected
                                                 
def test_view_character():
    value = Town_Menu(1)
    assert value == "option 1"

def test_view_map():
    value = Town_Menu(2)
    assert value == "option 2"

def test_move():
    value = Town_Menu(3)
    assert value == "option 3"

def test_rest():
    value = Town_Menu(4)
    assert value == "option 4"

def test_save_game():
    value = Town_Menu(5)
    assert value == "option 5" 

def test_exit_game():
    value = Town_Menu(6)
    assert value == "option 6"