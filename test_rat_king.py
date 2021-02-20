import pytest
import townMenu
import globalVar
import player
import tudtestbase

globalVar.test_mode = True #prevents menu function from looping

#def rat_king_appear():


def rat_king_combat_1():

    status = False

    globalVar.player.coordinate = 64

    globalVar.menu_choice = "1"

    tudtestbase.set_keyboard_input([""])

    townMenu.combat_menu()

    tudtestbase.get_display_output()

    for i in tudtestbase.print_values: #a list called print_values that store all prints
        if i == "\nYou deal " + "2" + " damage to the Rat": #check for print game exited
            status = True
        elif i == "\nYou deal " + "3" + " damage to the Rat": #check for print game exited
            status = True
        elif i == "\nYou deal " + "4" + " damage to the Rat": #check for print game exited
            status = True

    assert status == True

##def test_hero_health_amt():
##
##    globalVar.menu_choice = "1"
##
##    townMenu.combat_menu()
##
##    assert globalVar.player.hp < 20
##
def test_rat_dead():

    outdoor_menu = False

    globalVar.player.coordinate = 2

    globalVar.rat.hp = 1

    globalVar.combat_choice = "1"

    tudtestbase.set_keyboard_input([""])

    townMenu.combat_menu()

    tudtestbase.get_display_output()

    for i in tudtestbase.print_values: #a list called print_values that store all prints
        if i == "\nDay " + str(globalVar.day) + ": You are out in the open.": #check for print game exited
            outdoor_menu = True

    assert outdoor_menu == True
