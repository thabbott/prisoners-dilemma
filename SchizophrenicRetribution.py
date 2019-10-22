from random import random, choices

from Prisoner import Prisoner

"""
SchizophrenicRetribution: an old Prisoner who usually copies their
opponent's last choice, but forgets what to do as time goes on so
they usually just cooperate with anyone and everyone.
They won't stop telling you the same stories from their glory days
as a TitForTat.
"""
class SchizophrenicRetribution(Prisoner):
    def __init__(self):
        self.round_number = 0
        self.last_strategy = True

    def pick_strategy(self):
        r = random()

        # 0 < schizophrenic factor < 1 increases with round number
        # and maximum schizophrenia sets in after 100 rounds.
        sf = min(self.round_number / 100, 1)

        if r < (1 - 0.4*sf):
            return self.last_strategy
        else:
            return choices([True, False], weights=[4, 1])

    def process_results(self, my_strategy, other_strategy):
        self.round_number = self.round_number + 1
        self.last_strategy = other_strategy
