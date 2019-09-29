from Prisoner import Prisoner

"""
Jesus: a Prisoner who always cooperates
"""
class Jesus(Prisoner):
    
    name = "Jesus"
    
    def pick_strategy(self):
        return True
