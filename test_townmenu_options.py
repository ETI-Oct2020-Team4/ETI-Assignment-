import mainMenu
import globalVar
import pytest

globalVar.test_mode = True #Always put it there as true

# Test for Main menu
def test_Main_Menu_option_1():  # test option 1
    globalVar.menu_choice = "1"

    assert mainMenu.menu() == "1"


def test_Main_Menu_option_2():  # test option 2
    globalVar.menu_choice = "2"

    assert mainMenu.menu() == "2"


def test_Main_Menu_option_3():  # test option 3
    globalVar.menu_choice = "3"

    assert mainMenu.menu() == "3"


def test_Main_Menu_option_letters():  # test letters input
    globalVar.menu_choice = "a"

    assert mainMenu.menu() == "error"


def test_Main_Menu_option_SpecialCharacters():  # test special characters input
    globalVar.menu_choice = "$#@"

    assert mainMenu.menu() == "error"


def test_Main_Menu_option_Blank():  # test blank input
    globalVar.menu_choice = ""

    assert mainMenu.menu() == "error"
