from Prisoner import Prisoner
import numpy as np

class MasonPrisoner(Prisoner):
    def __init__(self):
        self.p = .5

    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """
    def pick_strategy(self):
        x = np.random.rand()
        if x > self.p:
            return True
        else:
            return False

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
        if other_strategy:
            self.p = .7
        else:
            self.p = .3
