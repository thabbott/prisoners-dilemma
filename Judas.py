from Prisoner import Prisoner
from Tournament import Tournament

"""
Judas: a Prisoner cooperates if they are winning and defects if they are losing.
"""
class Judas(Prisoner):
    
    def __init__(self):
        self.my_points = 0
        self.other_points = 0
        self.strat = True
        self.name = "Judas"
    
    def pick_strategy(self):
        return self.strat
    
    """
    This Prisoner keeps the score and sees if it is winning or not. If it is losing it      takes bigger risks and tries to catch up.
    """
    def process_results(self, my_strategy, other_strategy):
        self.my_points += Tournament.score(Tournament,my_strategy,other_strategy)[0]
        self.other_points += Tournament.score(Tournament,my_strategy,other_strategy)[1]
        if self.my_points>=self.other_points:
            self.strat = True
        else:
            self.strat = False