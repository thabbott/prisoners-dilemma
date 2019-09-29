"""
Prisoner superclass
"""
class Prisoner():
    
    """
    Prisoner's name
    """
    name = "Prisoner"

    """
    Constructor. Called once at the start of each match.
    Override this method to give your prisoner a name
    and, if needed, to initialize any 
    auxiliary data you want to use toto determine your 
    Prisoner's strategy. This data will persist between
    rounds of a match but not between matches.
    """
    def __init__(self):
        return self
    
    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """
    def pick_strategy(self):
        return True
    
    """
    Process the results of a round. This provides an opportunity to
    store data that preserves memory of previous rounds.
    
    Parameters
    ----------
    my_strategy: bool
        This Prisoner's strategy
        
    other_strategy: bool
        The opponent's strategy
    """
    def process_results(self, my_strategy, other_strategy):
        pass
