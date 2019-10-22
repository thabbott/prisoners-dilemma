from Prisoner import Prisoner
import random

class XmasTruce(Prisoner):

    def __init__(self):
        self.N = self.C = self.eC = self.D = self.ci = self.di = 0
        self.other_strategy = True # First move will be to cooperate!
        self.a = 0
    
    """
    # N is the total number of rounds we have done so far
    # C is the total number of times I have cooperated
    # eC is the total number of times my opponent has cooperated
    # D is the total number of times I have defected
    # ci is the number of times in a row I have cooperated
    # di is the number of times in a row I have defected
    """
    def pick_strategy(self):

        if self.N > 0:
            magic_number = self.ci * (self.C/self.N) 
        else:
            magic_number = 10

        if self.N%25 == 0: # if it's the mod(50)th round:
            self.a += 1 # advance the iterator
            return True # err on the side of cooperating
        
        elif self.N%25 < magic_number:
            if self.a%2 == 0:
                # Go on a mean streak
                return False
            else:
                # Go on a cooperative streak
                return True
        else: 
            return self.other_strategy # play tit for tat
    
    """
    This Prisoner also has to remember their opponent's last strategy
    """
    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == True:
            self.C += 1
            self.ci += 1
            self.di = 0
        elif my_strategy == False:
            self.D += 1
            self.di += 1
            self.ci = 0
        self.other_strategy = other_strategy
        if other_strategy == True:
            self.eC += 1



