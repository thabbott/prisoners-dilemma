from Prisoner import Prisoner

"""
Lucifer: a Prisoner who always defects.
"""
class Lucifer(Prisoner):
    
    def pick_strategy(self):
        return False
