import random
import globalVar
import player


def menu():
    if globalVar.player.has_orb:
        print("You found the Orb of Power!\nYour attack increases by 5!\nYour defence increases by 5!")

    if globalVar.player.coordinate in globalVar.towns_coordinates:
        print("\nDay " + str(globalVar.day) + ": You are in a town.")
    else:
        print("\nDay " + str(globalVar.day) + ": You are out in the open.")

    menu_options = ["1) View Character", "2) View Map", "3) Move"]
    if globalVar.player.coordinate in globalVar.towns_coordinates:
        menu_options += ["4) Rest", "5) Save", "6) Exit"]
    else:
        menu_options += ["4) Exit Game"]

    for option in menu_options:
        print(option)

    if globalVar.test_mode:
        menu_choice = globalVar.menu_choice
    else:
        menu_choice = input("Enter choice: ")

    if globalVar.player.coordinate in globalVar.towns_coordinates:
        if menu_choice == "1":
            view_character()
            if not globalVar.test_mode:
                menu()
            else:
                return "1"
        elif menu_choice == "2":
            view_map()
            if not globalVar.test_mode:
                menu()
            else:
                return "2"
        elif menu_choice == "3":
            move()
            return "3"
        elif menu_choice == "4":
            rest()
            if not globalVar.test_mode:
                menu()
            else:
                return "4"
        elif menu_choice == "5":
            save_game()
            if not globalVar.test_mode:
                menu()
            else:
                return "5"
        elif menu_choice == "6":
            if not globalVar.test_mode:
                exit()
            else:
                return "6"
        else:
            error = "Please enter a valid option"
            if not globalVar.test_mode:
                print(error)
                menu()
            else:
                return error
    else:
        if menu_choice == "1":
            view_character()
            if not globalVar.test_mode:
                menu()
            else:
                return "1"
        elif menu_choice == "2":
            view_map()
            if not globalVar.test_mode:
                menu()
            else:
                return "2"
        elif menu_choice == "3":
            move()
            return "3"
        elif menu_choice == "4":
            if not globalVar.test_mode:
                exit()
            else:
                return "4"
        else:
            error = "Please enter a valid option"
            if not globalVar.test_mode:
                print(error)
                menu()
            else:
                return error

    try:
        selected_option = menu_options[int(menu_choice) - 1]
        return selected_option
    except IndexError:
        return menu_options[0]


def view_character(player=globalVar.player):
    print("\n" + player.name)
    print("  Damage:" + player.damage)
    print(" Defence:" + str(player.defence))
    print("      HP:" + str(player.hp))

    if globalVar.player.has_orb:
        print("You are holding the Orb of Power.")


def view_map():
    def generate_board():
        board = {
            "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "",
            "9": "", "10": "", "11": "", "12": "", "13": "", "14": "", "15": "", "16": "",
            "17": "", "18": "", "19": "", "20": "", "21": "", "22": "", "23": "", "24": "",
            "25": "", "26": "", "27": "", "28": "", "29": "", "30": "", "31": "", "32": "",
            "33": "", "34": "", "35": "", "36": "", "37": "", "38": "", "39": "", "40": "",
            "41": "", "42": "", "43": "", "44": "", "45": "", "46": "", "47": "", "48": "",
            "49": "", "50": "", "51": "", "52": "", "53": "", "54": "", "55": "", "56": "",
            "57": "", "58": "", "59": "", "60": "", "61": "", "62": "", "63": "", "64": "",
        }

        board[str(globalVar.player.coordinate)] = " H "
        for town in globalVar.towns_coordinates:
            if town == globalVar.player.coordinate:
                board[str(town)] = "H/T"
            elif town == globalVar.orb_coordinate:
                if not globalVar.player.has_orb:
                    board[str(town)] = "T/O"
                else:
                    board[str(town)] = " T "
            else:
                board[str(town)] = " T "

        board[str(globalVar.king_rat.coordinate)] = " K "

        row1 = "|"
        row2 = "|"
        row3 = "|"
        row4 = "|"
        row5 = "|"
        row6 = "|"
        row7 = "|"
        row8 = "|"

        for i in range(1, 9):
            grid = board[str(i)]
            if grid == "":
                row1 += ("   " + "|")
            else:
                row1 += grid + "|"

        for i in range(9, 17):
            grid = board[str(i)]
            if grid == "":
                row2 += ("   " + "|")
            else:
                row2 += grid + "|"

        for i in range(17, 25):
            grid = board[str(i)]
            if grid == "":
                row3 += ("   " + "|")
            else:
                row3 += grid + "|"

        for i in range(25, 33):
            grid = board[str(i)]
            if grid == "":
                row4 += ("   " + "|")
            else:
                row4 += grid + "|"

        for i in range(33, 41):
            grid = board[str(i)]
            if grid == "":
                row5 += ("   " + "|")
            else:
                row5 += grid + "|"

        for i in range(41, 49):
            grid = board[str(i)]
            if grid == "":
                row6 += ("   " + "|")
            else:
                row6 += grid + "|"

        for i in range(49, 57):
            grid = board[str(i)]
            if grid == "":
                row7 += ("   " + "|")
            else:
                row7 += grid + "|"

        for i in range(57, 65):
            grid = board[str(i)]
            if grid == "":
                row8 += ("   " + "|")
            else:
                row8 += grid + "|"

        print("+---" * 8 + "+")
        print(row1)
        print("+---" * 8 + "+")
        print(row2)
        print("+---" * 8 + "+")
        print(row3)
        print("+---" * 8 + "+")
        print(row4)
        print("+---" * 8 + "+")
        print(row5)
        print("+---" * 8 + "+")
        print(row6)
        print("+---" * 8 + "+")
        print(row7)
        print("+---" * 8 + "+")
        print(row8)
        print("+---" * 8 + "+")

    generate_board()


def move():
    def error_message():
        print("Invalid Input")

    view_map()
    print("W = up; A = left, S = down; D = right;")

    if globalVar.test_mode:
        move_choice = globalVar.move_choice
    else:
        move_choice = input("Enter choice: ")

    move_choice = move_choice.upper()

    if move_choice == "W":
        if globalVar.player.coordinate > 8:
            globalVar.player.coordinate -= 8
            globalVar.day += 1
        else:
            error_message()
    elif move_choice == "A":
        if globalVar.player.coordinate not in [1, 9, 17, 25, 33, 41, 49, 57]:
            globalVar.player.coordinate -= 1
            globalVar.day += 1
        else:
            error_message()
    elif move_choice == "S":
        if globalVar.player.coordinate < 57:
            globalVar.player.coordinate += 8
            globalVar.day += 1
        else:
            error_message()
    elif move_choice == "D":
        if globalVar.player.coordinate not in [8, 16, 24, 32, 40, 48, 56, 64]:
            globalVar.player.coordinate += 1
            globalVar.day += 1
        else:
            error_message()
    else:
        if not globalVar.test_mode:
            error_message()
            move()
        else:
            return "Invalid Input"

    if globalVar.player.coordinate == globalVar.orb_coordinate:
        globalVar.player.has_orb = True
        current_damage = list(map(int, globalVar.player.damage.split("-")))
        globalVar.player.damage = str(current_damage[0] + 5) + "-" + str(current_damage[1] + 5)
        globalVar.player.defence += 5

    if globalVar.player.coordinate in globalVar.towns_coordinates:
        if not globalVar.test_mode:
            menu()
    elif globalVar.player.coordinate == globalVar.king_rat.coordinate:
        globalVar.rat = globalVar.king_rat
        combat_menu()
    else:
        globalVar.rat = player.Player("Encounter! - Rat", "1-3", 1, 10, 0, False)
        combat_menu()


def combat_menu():
    view_map()
    print("Day " + str(globalVar.day) + ": You are out in the open.")

    current_damage = list(map(int, globalVar.rat.damage.split("-")))
    inflict_damage = random.choice(range(current_damage[0], current_damage[1] + 1)) - globalVar.player.defence
    globalVar.player.hp -= inflict_damage

    print("\nOuch! The Rat hit you for " + str(inflict_damage) + " damage!")
    print("You have " + str(globalVar.player.hp) + " HP left.")

    view_character(globalVar.rat)

    print("1) Attack")
    print("2) Run")

    if globalVar.test_mode:
        menu_choice = globalVar.combat_choice
    else:
        menu_choice = input("Enter choice: ")

    if menu_choice == "1":
        current_damage = list(map(int, globalVar.player.damage.split("-")))
        inflict_damage = random.choice(range(current_damage[0], current_damage[1] + 1)) - globalVar.rat.defence

        if globalVar.rat.coordinate == 64 and globalVar.player.has_orb != True:
            inflict_damage = 0

        globalVar.rat.hp -= inflict_damage

        print("\nYou deal " + str(inflict_damage) + " damage to the Rat")

        if globalVar.player.hp > 0 and globalVar.day <= 30:
            if globalVar.rat.hp <= 0:
                view_character(player=globalVar.rat)
                print("The rat has been defeated.")

                if not globalVar.test_mode:
                    menu()
            else:
                combat_menu()
        else:
            print("\nIt has been " + str(globalVar.day) + " days.")
            view_character()
            print("GAME OVER")
    elif menu_choice == "2":
        menu()
    else:
        error = "Please enter a valid option"
        if not globalVar.test_mode:
            print(error)
            combat_menu()
        else:
            return error


def rest():
    if globalVar.player.hp != 20:
        globalVar.player.hp = 20
        globalVar.day += 1

        print("\nYou are fully healed.")
        return globalVar.player.hp
    else:
        error = "Error: Hero is unable to Rest"
        if not globalVar.test_mode:
            print(error)
            menu()
        else:
            return error


def save_game():
    f = open("gamesave.txt", "w")
    f.write(
        str(globalVar.day) + "," + globalVar.player.name + "," + globalVar.player.damage + "," +
        str(globalVar.player.defence) + "," + str(globalVar.player.hp) + "," + str(globalVar.player.coordinate) + "," +
        str(globalVar.player.has_orb)
    )
    f.close()

    print("\nGame saved.")
