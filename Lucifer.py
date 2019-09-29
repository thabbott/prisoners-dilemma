"""
Lucifer: a Prisoner who always defects.
"""
class Lucifer(Prisoner):
    
    name = "Lucifer"
    
    def pick_strategy(self):
        return False
