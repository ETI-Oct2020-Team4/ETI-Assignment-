import pytest
from Town_Menu import *

def test_character_stats_print():
    value = Show_Character_Stats()
    assert value == "The Hero2-4120"
