import random
from player import Player

test_mode = False

menu_choice = "1"
move_choice = "W"
combat_choice = "1"

day = 1
player = Player("The Hero", "2-4", 1, 20, 1, False)
rat = Player("Encounter! - Rat", "1-3", 1, 10, 0, False)
king_rat = Player("Encounter! - Rat King", "8-12", 5, 25, 64, False)

towns_coordinates = [1, 12, 22, 26, 53]
orb_coordinate = random.choice([12, 22, 26, 53])