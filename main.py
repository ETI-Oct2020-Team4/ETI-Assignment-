import globalVar


def menu():
    print("\nWelcome to Ratventure!\n----------------------")
    print("1) New Game")
    print("2) Resume Game")
    print("3) Exit Game")

    if globalVar.test_mode:
        menu_choice = globalVar.menu_choice
    else:
        menu_choice = input("Enter choice: ")

    if menu_choice == "1":
        new_game()
        return "1"
    elif menu_choice == "2":
        if resume_game():
            new_game()
            return "2"
        else:
            menu()
            print("Error: Game cannot be resumed")
            return "Error"
    elif menu_choice == "3":
        if not globalVar.test_mode:
            exit()
        else:
            return "3"
    else:
        error = "Please enter a valid option"
        if not globalVar.test_mode:
            print(error)
            menu()
        else:
            return error


def new_game():
    import townMenu
    print(townMenu.menu())


def resume_game():
    try:
        f = open("gamesave.txt", "r")
        save_data = f.read()
        save_data_components = save_data.split(",")
        globalVar.day = int(save_data_components[0])
        import player
        try:
            globalVar.player = player.Player(save_data_components[1], save_data_components[2],
                                             int(save_data_components[3]), int(save_data_components[4]),
                                             int(save_data_components[5]), eval(save_data_components[6]))

            return True
        except IndexError:
            print("\nInvalid gamesave.")
            return False

    except IOError:
        print("\nNo previous gamesaves found")
        return False


# Main
if not globalVar.test_mode:
    menu()
