from Prisoner import Prisoner

"""
Telepath: a Prisoner who can read (a limited number of opponents') minds
"""
class Telepath(Prisoner):

    """
    Track opponents' first two moves and the round number
    """
    def __init__(self):
        self.iround = 1
        self.opp_first_move = True
        self.opp_second_move = True

    """
    Strategy: defect on round 1, cooperate on round 2, and then
    try to identify your opponent on subsequent rounds and play accordingly
    """
    def pick_strategy(self):
        if self.iround == 1:
            return False
        elif self.iround == 2:
            return True
        else:
            if self.opp_first_move:
                if self.opp_second_move:
                    # Assume Jesus and defect
                    return False
                else:
                    # Assume TitForTat and defect
                    return False
            else:
                if self.opp_second_move:
                    # Assume Telepath and cooperate
                    return True
                else:
                    # Assume Lucifer and defect
                    return False


    """
    Record first two strategies
    """
    def process_results(self, my_strategy, other_strategy):
        if self.iround == 1:
            self.opp_first_move = other_strategy
        elif self.iround == 2:
            self.opp_second_move = other_strategy
        self.iround += 1
