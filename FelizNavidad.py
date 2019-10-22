from Prisoner import Prisoner
import random

class FelizNavidad(Prisoner):

    def __init__(self):
        self.N = self.C = self.ci = 0
        self.eC = 0
        self.other_strategy = True
    
    """
    N : the total number of rounds we have done so far
    C : the total number of times I have cooperated
    ci : the number of times in a row I have cooperated
    eC : the total number of times my opponent has cooperated
    
    """
    def pick_strategy(self):
         
        if self.ci > 5: # If I have cooperated a lot of times in a row
            if self.C/self.N > 0.6: # and I have cooperated a lot already
                return False # defect
            else:
                return True

        else:
            r = random.randint(0,9) # generate random number
            if r == 0:
                return self.other_strategy
            else:
                return True

    """
    This Prisoner also has to remember their opponent's last strategy
    """
    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == True:
            self.C += 1
            self.ci += 1

        elif my_strategy == False:

            self.ci = 0
        self.other_strategy = other_strategy
        if other_strategy == True:
            self.eC += 1



