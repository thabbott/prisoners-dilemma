from Prisoner import Prisoner
from numpy import random

"""
Random: a Prisoner who plays randomly
"""
class Random(Prisoner):

    def __init__(self):
        self.name = "Random"

    """
    This Prisoner always choses a random answer
    """
    def pick_strategy(self):
        return random.choice([-1,1])>0
