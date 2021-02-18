import townMenu
import globalVar

globalVar.test_mode = True

# Town Menu
def test_town_menu():
    globalVar.player.coordinate = 1

    menu_options = ["1) View Character (Default)", "2) View Map", "3) Move", "4) Rest", "5) Save", "6) Exit"]
    for choice in range(1, len(menu_options) + 1):
        globalVar.menu_choice = str(choice)
        assert townMenu.menu() == menu_options[choice - 1]

#Outdoor Menu
def test_outdoor_menu():
    globalVar.player.coordinate = 2

    menu_options = ["1) View Character (Default)", "2) View Map", "3) Move", "4) Exit Game"]
    for choice in range(1, len(menu_options) + 1):
        globalVar.menu_choice = str(choice)
        assert townMenu.menu() == menu_options[choice - 1]