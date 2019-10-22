from Prisoner import Prisoner
from Tournament import Tournament

"""
Inv_Judas: a Prisoner cooperates if they are losing and defects if they are winning.
"""
class Inv_Judas(Prisoner):
    
    def __init__(self):
        self.my_points = 0
        self.other_points = 0
        self.strat = True
        self.name = "Inv_Judas"
    
    def pick_strategy(self):
        return self.strat
    

    def process_results(self, my_strategy, other_strategy):
        self.my_points += Tournament.score(Tournament,my_strategy,other_strategy)[0]
        self.other_points += Tournament.score(Tournament,my_strategy,other_strategy)[1]
        if self.my_points>=self.other_points:
            self.strat = False
        else:
            self.strat = True